from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    description = models.TextField(max_length=2500, verbose_name="توضیحات")
    gallery = models.ManyToManyField(to='BlogGallery', verbose_name="وبلاگ", related_name="back_gallery")
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"

    class Meta:
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ ها"
        # ordering = ["-created"]


class BlogGallery(models.Model):
    image = models.ImageField(upload_to="blog", verbose_name="تصویر")

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "گالری وبلاگ"
        verbose_name_plural = "گالری وبلاگ ها"
