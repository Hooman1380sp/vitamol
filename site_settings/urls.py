from django.urls import path
from .views import HiringCreateView,ContactUsCreateView
app_name = ""

urlpatterns = [
    path("hiring/",HiringCreateView.as_view()),
    path("contact-us/",ContactUsCreateView.as_view()),
]