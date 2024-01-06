from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Product, ProductCategory
from .serializers import ProductSerializer, ProductCategorySerializer


# Product
class ProductListView(APIView):
    serializer_class = ProductSerializer

    def get(self, request, id):
        category = get_object_or_404(ProductCategory, id=id)
        product = Product.objects.filter(category=category.id)
        ser_data = ProductSerializer(instance=product,many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)

class ProductDetailView(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"


# productCategory
# class ProductCategoryListView(ListAPIView):
#     serializer_class = ProductCategorySerializer
#     queryset = ProductCategory.objects.all()


class ProductCategoryDetailView(APIView):
    serializer_class = ProductCategorySerializer

    def get(self, request, id):
        category = get_object_or_404(ProductCategory, id=id)
        subcategory = category.subcategory.all()
        ser_data = self.serializer_class(instance=subcategory, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)



