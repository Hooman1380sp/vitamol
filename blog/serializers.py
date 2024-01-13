from rest_framework import serializers
from .models import Blog, BlogGallery


class BlogSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("name", "description", "image")

    def get_image(self, obj: Blog):
        result = obj.back_blog.all()
        return GalleryBlogSerializer(instance=result, many=True).data


class GalleryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogGallery
        fields = ("blog", "image", "thumbnail")
