from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from .models import Hiring,ContactUs
from .serializers import HiringSerializer,ContactUsSerializer

class HiringCreateView(CreateAPIView):
    serializer_class = HiringSerializer
    queryset = Hiring.objects.all()

class ContactUsCreateView(CreateAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()