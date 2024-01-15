from django.db import models
from imagekit.processors import ResizeToFit
from imagekit.models import ImageSpecField


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    description = models.TextField(max_length=2500, verbose_name="توضیحات")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"

    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ ها"
        # ordering = ["-created"]


class BlogGallery(models.Model):
    blog = models.ForeignKey(to="Blog", on_delete=models.CASCADE, verbose_name="وبلاگ", related_name="back_blog")
    image = models.ImageField(upload_to="blog", verbose_name="تصویر")
    thumbnail = ImageSpecField(source="image", processors=[ResizeToFit(width=235, height=330)], options={"quality": 80})
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.blog.title}"

    class Meta:
        verbose_name = "گالری وبلاگ"
        verbose_name_plural = "گالری وبلاگ ها"
