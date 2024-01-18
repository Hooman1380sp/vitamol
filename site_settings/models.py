from django.db import models

# Create your models here.


# hiring


class Hiring(models.Model):
    fullname = models.CharField(max_length=300, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=13, verbose_name="شماره تماس", db_index=True)
    email = models.EmailField(max_length=150, verbose_name="ایمیل", null=True, blank=True)
    description = models.TextField(max_length=1500, verbose_name="توضیحات")
    pdf_file = models.FileField(upload_to="hiring", verbose_name="فایل PDF")

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    class Meta:
        verbose_name = "بخش استخدام"
        verbose_name_plural = "بخش استخدامی ها"


# contact us


class ContactUs(models.Model):
    fullname = models.CharField(max_length=300, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=13, verbose_name="شماره تماس", db_index=True)
    email = models.EmailField(max_length=150, verbose_name="ایمیل", null=True, blank=True)
    day = models.PositiveSmallIntegerField(verbose_name="روز هفته")
    hour = models.CharField(max_length=40, verbose_name="ساعت")

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "بخش تماس با ما"
