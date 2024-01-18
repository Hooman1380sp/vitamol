from django.db import models

# Create your models here.


# hiring

class Hiring(models.Model):
    fullname = models.CharField(max_length=300,verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=13,verbose_name="شماره تماس",db_index=True)
    email = models.EmailField(max_length=150,verbose_name="ایمیل",null=True,blank=True)
    description = models.TextField(max_length=1500,verbose_name="توضیحات")
    pdf_file = models.FileField(upload_to='hiring',verbose_name="فایل PDF")

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    class Meta:
        verbose_name = "بخش استخدام"
        verbose_name_plural = "بخش استخدامی ها"
