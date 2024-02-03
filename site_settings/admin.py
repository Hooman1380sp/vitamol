from django.contrib import admin
from .models import Hiring, ContactUs, RegisterFake, Event, EventGallery

# Register your models here.

admin.site.register(Hiring)
admin.site.register(ContactUs)
admin.site.register(RegisterFake)
admin.site.register(Event)
admin.site.register(EventGallery)
