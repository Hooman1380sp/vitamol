from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    description = models.TextField(max_length=2500, verbose_name="توضیحات")
    gallery = models.ManyToManyField(
        to="BlogGallery",
        verbose_name="تصاویر",
        related_name="back_gallery",
        help_text="(اندازه پیش فرض تصاویر بلاگ به صورت width=464px و height=637px است که تجریحا باید به فرمت webp یا درغیر اینصورت jpg و jpeg برای فشرده بودن حجم آن باشد. حجم تصویر پست بلاگ می تواند تا یک مگابایت باشد اما بهتر است که برای سرعت بیشتر لود، حجم به مراتب کمتری استفاده شود. برای اندازه تصویر الزامی نیست اما حتما باید ارتفاع(height) بیشتر از عرض(width) آن باشد. یعنی تصویر به صورت عمودی باشد)",
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"

    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ ها"
        # ordering = ["-created"]


class BlogGallery(models.Model):
    original_image = models.ImageField(upload_to="original_blog/", verbose_name="تصویر")
    resized_image = ProcessedImageField(
        upload_to="resized_blog/",
        processors=[ResizeToFit(width=235, height=330)],
        # format='JPEG',
        # options={'quality': 90},
        verbose_name="تصویر",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "گالری وبلاگ"
        verbose_name_plural = "گالری وبلاگ ها"
