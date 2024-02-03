# Generated by Django 5.0 on 2024-02-03 20:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_settings", "0003_eventgallery_alter_registerfake_description_event"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventgallery",
            options={"verbose_name": "تصاویر", "verbose_name_plural": "تصاویر رویداد"},
        ),
        migrations.AlterField(
            model_name="event",
            name="gallery_event",
            field=models.ManyToManyField(
                help_text="(اندازه پیش فرض تصاویر بنر اصلی سایت به صورت width=395px و height=549px است که تجریحا باید به فرمت webp یا درغیر اینصورت jpg و jpeg برای فشرده بودن حجم آن باشد. بهتر است حجم تصاویر نهایتا 150 الی 200 کیلوبایت باشند. برای اندازه تصویر الزامی نیست اما حتما باید ارتفاع(height) بیشتر از عرض(width) آن باشد. یعنی تصویر به صورت عمودی باشد)",
                to="site_settings.eventgallery",
                verbose_name="تصویر",
            ),
        ),
        migrations.AlterField(
            model_name="eventgallery",
            name="image",
            field=models.ImageField(upload_to="event", verbose_name="تصویر"),
        ),
    ]
