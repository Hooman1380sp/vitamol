from django.db import models


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
    day = models.CharField(max_length=40, verbose_name="روز هفته")
    hour = models.CharField(max_length=40, verbose_name="ساعت")

    def __str__(self):
        return f"{self.fullname} - {self.phone}"

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "بخش تماس با ما"


# register(Fake)


class RegisterFake(models.Model):
    name = models.CharField(max_length=150, verbose_name="نام", db_index=True)
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=13, verbose_name="شماره تماس", db_index=True)
    description = models.TextField(max_length=1000, verbose_name="توضیحات", null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.last_name)

    class Meta:
        verbose_name = "کاربران ثبت نامی"
        verbose_name_plural = "کاربران ثبت نامی ها"


# event


class Event(models.Model):
    description = models.CharField(max_length=250, verbose_name="توضیحات")
    gallery_event = models.ManyToManyField(
        to="EventGallery",
        verbose_name="تصویر",
        help_text="(اندازه پیش فرض تصاویر بنر اصلی سایت به صورت width=395px و height=549px است که تجریحا باید به فرمت webp یا درغیر اینصورت jpg و jpeg برای فشرده بودن حجم آن باشد. بهتر است حجم تصاویر نهایتا 150 الی 200 کیلوبایت باشند. برای اندازه تصویر الزامی نیست اما حتما باید ارتفاع(height) بیشتر از عرض(width) آن باشد. یعنی تصویر به صورت عمودی باشد)",
    )

    def __str__(self):
        return self.description[:40]

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"


class EventGallery(models.Model):
    image = models.ImageField(upload_to="event", verbose_name="تصویر")

    class Meta:
        verbose_name = "تصاویر"
        verbose_name_plural = "تصاویر رویداد"
