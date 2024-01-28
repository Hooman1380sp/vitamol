from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from .models import Hiring,ContactUs
from .serializers import HiringSerializer,ContactUsSerializer

class HiringCreateView(APIView):
    serializer_class = HiringSerializer

    def post(self, request):
        ser_data = self.serializer_class(data=request.data)
        ser_data.is_valid(raise_exception=True)
        ser_data.save()
        return Response(data=ser_data.data,status=status.HTTP_201_CREATED)

class ContactUsCreateView(CreateAPIView):
    serializer_class = ContactUsSerializer
    queryset = ContactUs.objects.all()