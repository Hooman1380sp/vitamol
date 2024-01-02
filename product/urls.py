from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductCategoryListView,
    ProductCategoryDetailView,
    ProductGalleryDetailView,
)


app_name = "product"

urlpatterns = [
    path("product-list/", ProductListView.as_view()),
    path("product-detail/<int:id>", ProductDetailView.as_view()),
    path("product-category-list/", ProductCategoryListView.as_view()),
    path("product-category/<int:id>", ProductCategoryDetailView.as_view()),
    path("product-gallery/<int:id>", ProductGalleryDetailView.as_view()),
]
