from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from products.models import Product
from shop.models import Shop


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Пользователь')
    dt = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.BooleanField(verbose_name='Статус', default=False)

    def __str__(self):
        return 'Заказ: {}'.format(self.id)

    class Meta:
        ordering = ('-dt', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True,
                              blank=True, verbose_name='Пользователь',
                              related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True,
                                blank=True, verbose_name='Товар')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Магазин')
    quantity = models.PositiveIntegerField(verbose_name='Количество',
                                           default=1)

    def __str__(self):
        return self.id


# https://webdevblog.ru/modelirAovanie-polimorfizma-v-django/
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Пользователь')


class Phone(Contact):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер должен быть в формате: '+70000000'. Поддерживается до 15 цифр.")
    phone = models.CharField(validators=[phone_regex], max_length=17,
                             blank=True, verbose_name='Номер телефона')


class Address(Contact):
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    house = models.PositiveIntegerField(verbose_name='Дом')
    apartment = models.PositiveIntegerField(verbose_name='Квартира')




