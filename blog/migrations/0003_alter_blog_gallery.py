# Generated by Django 5.0 on 2024-01-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_remove_bloggallery_blog_remove_bloggallery_created_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="gallery",
            field=models.ManyToManyField(
                related_name="back_gallery",
                to="blog.bloggallery",
                verbose_name="تصاویر",
            ),
        ),
    ]
