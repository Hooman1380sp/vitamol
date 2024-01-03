from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=226, verbose_name="نام")
    parent_category = models.ForeignKey(to="self", on_delete=models.CASCADE, null=True, blank=True, editable=True)
    # slug = models.SlugField(max_length=500, verbose_name="آدرس اینترنتی", unique=True)
    image = models.ImageField(upload_to="product", verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f'{self.name} - {self.id}'
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'



class Product(models.Model):
    name = models.CharField(max_length=226, verbose_name="نام محصول")
    category = models.ManyToManyField(to=ProductCategory, verbose_name="دسته بندی", related_name="category_back")
    description = models.TextField(max_length=7000, verbose_name="توضیحات")
    # price = models.IntegerField(verbose_name="قیمت", null=True, blank=True)
    # slug = models.SlugField(unique=True, verbose_name="آدرس اینترنتی", max_length=500, db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f'{self.name} - {self.id}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

class ProductGallery(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name="محصول", related_name="product_back")
    image = models.ImageField(upload_to="product", verbose_name="تصویر")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f'{self.product} - {self.created}'
    class Meta:
        verbose_name = 'گالری محصول'
        verbose_name_plural = 'گالری محصولات'