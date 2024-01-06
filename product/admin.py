from django.contrib import admin
from .models import Product, ProductCategory, ProductGallery
from mptt.admin import MPTTModelAdmin

admin.site.register(Product)
admin.site.register(ProductGallery)
admin.site.register(ProductCategory, MPTTModelAdmin)
