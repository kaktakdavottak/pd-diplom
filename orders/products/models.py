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


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)
    category = models.ForeignKey(Category, related_name='products', blank=True,
                                 on_delete=models.SET_NULL,
                                 verbose_name='Категория товара', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                verbose_name='Товар')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,
                             verbose_name='Магазин')
    model = models.CharField(verbose_name='Модель', max_length=150)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_rrc = models.PositiveIntegerField(verbose_name='РРЦ')


