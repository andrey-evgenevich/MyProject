from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", blank=True, null=True
    )
    photo = models.ImageField(upload_to="product/photo", blank=True, null=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(verbose_name="Цена продукта", blank=True, null=True)
    date_create = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    date_change = models.DateTimeField(
        verbose_name="Дата последнего изменения", blank=True, null=True
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name

    def get_active_version(self):
        return self.versions.filter(is_current=True).first()


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Наименование продукта",
        related_name="version",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    version_number = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии продукта",
        help_text="Введите номер версии продукта",
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Наименование версии продукта",
        help_text="Введите наименование версии продукта",
    )
    is_current = models.BooleanField(
        verbose_name="признак текущей версии", help_text="Версия активна?", default=True
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.SET_NULL, null=True, blank=True,)


class Meta:
    verbose_name = "Версия"
    verbose_name_plural = "Версии"
    ordering = ["product", "version_name", "version_number"]
