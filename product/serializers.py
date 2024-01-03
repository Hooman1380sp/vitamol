from rest_framework import serializers
from .models import Product, ProductGallery, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "category", "description")


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("name", "image", "parent_category")


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ("product", "image")
