# Generated by Django 5.0 on 2024-02-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("site_settings", "0002_registerfake"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="event", verbose_name="")),
            ],
            options={
                "verbose_name": "تصاویر",
                "verbose_name_plural": "همه تصاویر",
            },
        ),
        migrations.AlterField(
            model_name="registerfake",
            name="description",
            field=models.TextField(
                blank=True, max_length=1000, null=True, verbose_name="توضیحات"
            ),
        ),
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.CharField(max_length=250, verbose_name="توضیحات"),
                ),
                (
                    "gallery_event",
                    models.ManyToManyField(
                        to="site_settings.eventgallery", verbose_name="تصویر"
                    ),
                ),
            ],
            options={
                "verbose_name": "رویداد",
                "verbose_name_plural": "رویدادها",
            },
        ),
    ]
