# Generated by Django 5.0 on 2024-02-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="gallery",
            field=models.ManyToManyField(
                help_text="(اندازه پیش فرض تصاویر بلاگ به صورت width=464px و height=637px است که تجریحا باید به فرمت webp یا درغیر اینصورت jpg و jpeg برای فشرده بودن حجم آن باشد. حجم تصویر پست بلاگ می تواند تا یک مگابایت باشد اما بهتر است که برای سرعت بیشتر لود، حجم به مراتب کمتری استفاده شود. برای اندازه تصویر الزامی نیست اما حتما باید ارتفاع(height) بیشتر از عرض(width) آن باشد. یعنی تصویر به صورت عمودی باشد)",
                related_name="back_gallery",
                to="blog.bloggallery",
                verbose_name="تصاویر",
            ),
        ),
    ]