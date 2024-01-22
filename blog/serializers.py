from rest_framework import serializers
from .models import Blog, BlogGallery


class BlogSerializerList(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("title", "description", "images", "id")

    def get_description(self, obj):
        return obj.description[:50]

    def get_images(self, obj):
        result = obj.gallery.all()
        return GalleryBlogSerializerReSizedImage(instance=result, many=True).data


class BlogSerializerDetail(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ("title", "description", "images", "id")

    def get_images(self, obj):
        result = obj.gallery.all()
        return GalleryBlogSerializerOriginalImage(instance=result, many=True).data


class GalleryBlogSerializerOriginalImage(serializers.ModelSerializer):
    class Meta:
        model = BlogGallery
        fields = ("original_image",)


class GalleryBlogSerializerReSizedImage(serializers.ModelSerializer):
    class Meta:
        model = BlogGallery
        fields = ("resized_image",)
