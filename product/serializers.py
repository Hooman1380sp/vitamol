from rest_framework import serializers
from .models import Product, ProductGallery, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "category", "description","images")

    def get_images(self, obj):
        result = obj.product_back.all()
        return ProductGallerySerializer(instance=result, many=True).data


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("name", "image", "parent")


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ("product", "image")
