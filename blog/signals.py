from django.dispatch import receiver
from .models import BlogGallery
from django.db.models.signals import post_save


@receiver(post_save, sender=BlogGallery)
def create_object_m2m(sender, **kwargs):
    instance = kwargs.get("instance")
    BlogGallery.objects.update(resized_image=instance.original_image)