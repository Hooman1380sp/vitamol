from rest_framework import serializers
from .models import Blog, BlogGallery


class BlogSerializerList(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("title", "description", "images","id")

    def get_description(self, obj):
        return obj.description[:50]

    def get_images(self, obj):
        result = obj.gallery.all()
        return GalleryBlogSerializer(instance=result, many=True).data

class BlogSerializerDetail(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("title", "description", "images","id")

    def get_images(self, obj):
        result = obj.gallery.all()
        return GalleryBlogSerializer(instance=result, many=True).data

class GalleryBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogGallery
        fields = ("image",)
