from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import Blog, BlogGallery
from .serializers import BlogSerializerList, BlogSerializerDetail


class BlogListView(APIView):
    serializer_class = BlogSerializerList

    def get(self, request):
        blogs = Blog.objects.all()
        ser_data = self.serializer_class(instance=blogs, many=True)
        return Response(data=ser_data.data, status=status.HTTP_200_OK)


class BlogDetailView(RetrieveAPIView):
    serializer_class = BlogSerializerDetail
    queryset = Blog.objects.all()
    lookup_field = "id"
