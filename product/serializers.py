from rest_framework import serializers
from .models import Product, ProductGallery, ProductCategory


class ProductSerializerList(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "category", "description", "images", "id")

    def get_images(self, obj):
        result = obj.gallery.all()
        return ProductGallerySerializer(instance=result, many=True).data

class ProductSerializerDetail(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "category", "description", "images", "field", "id")

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
