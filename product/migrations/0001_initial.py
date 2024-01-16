# Generated by Django 5.0 on 2024-01-13 20:27

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
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
                ("name", models.CharField(max_length=226, verbose_name="نام")),
                ("image", models.ImageField(upload_to="product", verbose_name="تصویر")),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
                (
                    "parent",
                    mptt.fields.TreeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subcategory",
                        to="product.productcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "دسته بندی محصول",
                "verbose_name_plural": "دسته بندی محصولات",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=226, verbose_name="نام محصول")),
                (
                    "description",
                    models.TextField(max_length=7000, verbose_name="توضیحات"),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "category",
                    models.ManyToManyField(
                        related_name="category_back",
                        to="product.productcategory",
                        verbose_name="دسته بندی",
                    ),
                ),
            ],
            options={
                "verbose_name": "محصول",
                "verbose_name_plural": "محصولات",
            },
        ),
        migrations.CreateModel(
            name="ProductGallery",
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
                ("image", models.ImageField(upload_to="product", verbose_name="تصویر")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد"),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_back",
                        to="product.product",
                        verbose_name="محصول",
                    ),
                ),
            ],
            options={
                "verbose_name": "گالری محصول",
                "verbose_name_plural": "گالری محصولات",
            },
        ),
    ]