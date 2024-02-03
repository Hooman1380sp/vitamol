from django.urls import path
from .views import HiringCreateView, ContactUsCreateView, RegisterFakeCreateView, EventDetailView

app_name = ""

urlpatterns = [
    path("hiring/", HiringCreateView.as_view()),
    path("contact-us/", ContactUsCreateView.as_view()),
    path("register/", RegisterFakeCreateView.as_view()),
    path("event/", EventDetailView.as_view()),
]
