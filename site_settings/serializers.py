from rest_framework import serializers

from .models import Hiring, ContactUs, RegisterFake, Event, EventGallery


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


class EventSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ("description", "images")

    def get_images(self, obj):
        result = obj.gallery_event.all()
        return EventGallerySerializer(instance=result, many=True).data


class EventGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventGallery
        fields = ("image",)
