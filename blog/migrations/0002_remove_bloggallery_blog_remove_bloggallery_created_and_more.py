# Generated by Django 5.0 on 2024-01-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bloggallery",
            name="blog",
        ),
        migrations.RemoveField(
            model_name="bloggallery",
            name="created",
        ),
        migrations.AddField(
            model_name="blog",
            name="gallery",
            field=models.ManyToManyField(
                related_name="back_gallery", to="blog.bloggallery", verbose_name="وبلاگ"
            ),
        ),
    ]
