from django.db import models


class Bllog(models.Model):
    title = models.CharField(max=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", blank=True)
    time_completed = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_pablished = models.BooleanField(default=Tue)
    cat = models.ForeignKey('Cdtegory', on_delete=models.PROTECT)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,db_index=True)

    def __str__(self):
        return self.name