from rest_framework import serializers
from .models import Blog, BlogGallery


class BlogSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("title", "description", "images")

    def get_images(self, obj):
        result = obj.back_blog.all()
        return GalleryBlogSerializer(instance=result, many=True).data


class GalleryBlogSerializer(serializers.ModelSerializer):
    # thumbnail = serializers.ImageField()
    class Meta:
        model = BlogGallery
        fields = ("blog", "image")
