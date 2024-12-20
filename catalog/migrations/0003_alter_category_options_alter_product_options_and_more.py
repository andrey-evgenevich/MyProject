# Generated by Django 5.1.1 on 2024-09-29 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="manufactured_at",
        ),
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание категории"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="catalog.category",
                verbose_name="Категория продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_change",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата последнего изменения"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="date_create",
            field=models.DateField(blank=True, null=True, verbose_name="Дата создания"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, null=True, verbose_name="Описание продукта"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Цена продукта"
            ),
        ),
    ]
