from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Наименование продукта',
                            help_text='Введите наименование продукта')
    description = models.TextField(verbose_name='Описание продукта')
    photo = models.ImageField(upload_to='product/photo',
                              blank=True,
                              null=True)
    category = models.CharField(max_length=100,
                                verbose_name='Категория продукта')
    price = models.IntegerField(verbose_name='Наименование продукта')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_change = models.DateTimeField(verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта',
                                           blank=True,
                                           null=True)

    class Meta:
        verbose_name = "Продукт"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Наименование категории',
                            help_text='Введите наименование категории')
    description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = "Категория"
        ordering = ["name"]

    def __str__(self):
        return self.name
