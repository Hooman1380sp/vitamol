from rest_framework import serializers
from .models import Hiring, ContactUs, RegisterFake


class HiringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hiring
        fields = ("fullname", "phone", "description", "email", "pdf_file")


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ("fullname", "phone", "email", "day", "hour")


class RegisterFakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterFake
        fields = ("name", "last_name", "phone", "description")
