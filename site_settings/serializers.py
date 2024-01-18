from rest_framework import serializers
from .models import Hiring, ContactUs


class HiringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiring
        fields = ("fullname", "phone", "description", "email", "pdf_file")


class ContancUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("fullname", "phone", "email", "day", "hour")
