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

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Информация о товаре'
        verbose_name_plural = 'Информация о товарах'


class Parameter(models.Model):
    name = models.CharField(verbose_name='Параметр', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'


class ProductParameter:
    product_info = models.ForeignKey(ProductInfo, on_delete=models.CASCADE,
                                     verbose_name='Информация о товаре')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE,
                                  verbose_name='Параметр')
    value = models.CharField(verbose_name='Значение', max_length=100)

    def __str__(self):
        return '{0}_{1}'.format(self.parameter, self.value)

    class Meta:
        verbose_name = 'Параметр товара'
        verbose_name_plural = 'Параметры товара'

