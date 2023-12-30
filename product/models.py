from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=226, verbose_name="نام")
    parent_category = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True, editable=True)
    slug = models.SlugField(max_length=500, verbose_name="", unique=True)
    image = models.ImageField(upload_to="image/category", null=True, blank=True, verbose_nam="")


class Product(models.Model):
    name = models.CharField(max_length=226, verbose_name="نام محصول")
    category = models.ManyToManyField(to=ProductCategory, verbose_name="", related_name="category_back")
    description = models.TextField(max_length=7000, verbose_name="توضیحات")
    image = models.ImageField(upload_to="image/product", null=True, blank=True)
    # price = models.IntegerField(verbose_name="قیمت", null=True, blank=True)
    slug = models.SlugField(unique=True, verbose_name="آدرس اینترنتی", max_length=500, db_index=True)


