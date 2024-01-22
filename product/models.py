from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=226, verbose_name="نام")
    parent = TreeForeignKey(
        to="self", on_delete=models.SET_NULL, null=True, blank=True, editable=True, related_name="subcategory"
    )
    # slug = models.SlugField(max_length=500, verbose_name="آدرس اینترنتی", unique=True)
    image = models.ImageField(upload_to="product", verbose_name="تصویر", null=True, blank=True)

    class MPTTMeta:
        order_insertions_by = ["name"]

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "دسته بندی محصول"
        verbose_name_plural = "دسته بندی محصولات"


class Product(models.Model):
    name = models.CharField(max_length=226, verbose_name="نام محصول")
    category = models.ManyToManyField(to=ProductCategory, verbose_name="دسته بندی", related_name="category_back")
    description = models.TextField(max_length=1200, verbose_name="توضیحات کوتاه",null=True,blank=True)
    field = models.TextField(max_length=4000,verbose_name="توضیحات",null=True,blank=True)
    # price = models.IntegerField(verbose_name="قیمت", null=True, blank=True)
    # slug = models.SlugField(unique=True, verbose_name="آدرس اینترنتی", max_length=500, db_index=True)
    gallery = models.ManyToManyField(to="ProductGallery", verbose_name="تصاویر محصولات", related_name="gallery_back")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.name} - {self.id}"

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class ProductGallery(models.Model):
    image = models.ImageField(upload_to="product", verbose_name="تصویر")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "گالری محصول"
        verbose_name_plural = "گالری محصولات"
