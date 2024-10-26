from django.db import models


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
    date_create = models.DateField(verbose_name="Дата создания", blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотры")

    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ["name"]

    def __str__(self):
        return self.name

