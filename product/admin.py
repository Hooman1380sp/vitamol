from django.contrib import admin
from .models import Product, ProductCategory, ProductGallery

admin.site.register(Product)
admin.site.register(ProductGallery)
admin.site.register(ProductCategory)