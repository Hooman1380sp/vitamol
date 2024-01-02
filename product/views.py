from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from .models import Product,ProductGallery,ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer, ProductGallerySerializer


# Product
class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'

# productCategory
class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class ProductCategoryDetailView(RetrieveAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    lookup_field = 'slug'

class ProductGalleryDetailView(RetrieveAPIView):
    serializer_class = ProductGallerySerializer
    queryset = ProductGallery.objects.all()