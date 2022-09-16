from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(blank=True, verbose_name="Контент")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-time_created"]


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
