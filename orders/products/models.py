from django.db import models
from shop.models import Shop


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)
    shops = models.ManyToManyField(Shop, related_name='categories',
                                   verbose_name='Магазины')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

