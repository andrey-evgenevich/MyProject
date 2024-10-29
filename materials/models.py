from django.db import models
from django.utils import timezone
from django import forms


class Materials(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="slug",
        null=True,
        blank=True,
    )
    content = models.TextField(
        max_length=50,
        verbose_name="содержимое",
        help_text="Введите содержимое",
    )
    photo = models.ImageField(upload_to="product/photo", blank=True, null=True)
    date_create = models.DateField(default=timezone.now, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ["name"]

        widgets = {
            'views_count': forms.NumberInput(
                attrs={'readonly': True, 'disabled': True}
            )
        }

    def __str__(self):
        return self.name

