from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class ProductCategory(MPTTModel):
    name = models.CharField(max_length=226, verbose_name="نام")
    parent = TreeForeignKey(
        to="self", on_delete=models.SET_NULL, null=True, blank=True, editable=True, related_name="subcategory"
    )
    # slug = models.SlugField(max_length=500, verbose_name="آدرس اینترنتی", unique=True)
    image = models.ImageField(
        upload_to="product",
        verbose_name="تصویر",
        null=True,
        blank=True,
        help_text="اندازه پیش فرض تصاویر کتگوری ها به صورت width=203px و height=241px است که تجریحا باید به فرمت webp یا درغیر اینصورت jpg و jpeg برای فشرده بودن حجم آن باشد. بهتر است حجم تصاویر نهایتا 50 الی 100 کیلوبایت باشند. برای اندازه تصویر الزامی نیست اما حتما باید ارتفاع(height) بیشتر از عرض(width) آن باشد. یعنی تصویر به صورت عمودی باشد",
    )

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
    description = models.TextField(max_length=1200, verbose_name="توضیحات کوتاه", null=True, blank=True)
    field = models.TextField(max_length=4000, verbose_name="توضیحات", default="long description")
    # price = models.IntegerField(verbose_name="قیمت", null=True, blank=True)
    # slug = models.SlugField(unique=True, verbose_name="آدرس اینترنتی", max_length=500, db_index=True)
    gallery = models.ManyToManyField(
        to="ProductGallery",
        verbose_name="تصاویر محصولات",
        related_name="gallery_back",
        help_text="(اندازه تصاویر باید در کمترین حالت ممکن با عرض(width) = 400px بارگذاری شوند تا کیفیت لازمه رو در حداقل ترین حالت ممکنه فراهم کنند. تصاویر حتما باید webp یا png با پس زمینه transparent باشند. بهتر است حجم تصاویر نهایتا 50 الی 100 کیلوبایت باشند.(هرچه کمتر سرعت لود بیشتر))",
    )
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
