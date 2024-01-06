from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCategoryDetailView,
)


app_name = "product"

urlpatterns = [
    path("product-list/<int:id>/", ProductListView.as_view()),
    path("product-detail/<int:id>/", ProductDetailView.as_view()),
    path("subcategory/<int:id>/", ProductCategoryDetailView.as_view()),
]
