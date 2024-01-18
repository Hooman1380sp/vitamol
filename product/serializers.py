from rest_framework import serializers
from .models import Product, ProductGallery, ProductCategory


class ProductSerializerList(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "category", "description", "images")

    def get_description(self, obj):
        return obj.description[:50]

    def get_images(self, obj):
        result = obj.gallery.all()
        return ProductGallerySerializer(instance=result, many=True).data


class ProductSerializerDetail(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "category", "description", "images")

    def get_images(self, obj):
        result = obj.gallery.all()
        return ProductGallerySerializer(instance=result, many=True).data


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "name", "image")


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ("image",)
