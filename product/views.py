from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Product, ProductCategory
from .serializers import ProductSerializerList,ProductSerializerDetail, ProductCategorySerializer


# Product
class ProductListView(APIView):
    """enter id(category) and take it products that related of category!"""

    serializer_class = ProductSerializerList

    def get(self, request, id):
        category = get_object_or_404(ProductCategory, id=id)
        product = Product.objects.filter(category=category.id)
        ser_data = self.serializer_class(instance=product, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class ProductDetailView(RetrieveAPIView):
    """enter id(product) and get"""

    serializer_class = ProductSerializerDetail
    queryset = Product.objects.all()
    lookup_field = "id"


class ProductCategoryDetailView(APIView):
    """get id(parent category) and take whole(subcategory)"""

    serializer_class = ProductCategorySerializer

    def get(self, request, id):
        category = get_object_or_404(ProductCategory, id=id)
        subcategory = category.subcategory.all()
        ser_data = self.serializer_class(instance=subcategory, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)
