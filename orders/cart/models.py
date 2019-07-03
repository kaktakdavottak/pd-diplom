from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from products.models import Product
from shop.models import Shop


class Order(models.Model):
    STATUS_NEW = 'New'
    STATUS_CONFIRMED = 'Confirmed'
    STATUS_COMPILED = 'Compiled'
    STATUS_SHIPPED = 'Shipped'
    STATUS_DELIVERED = 'Delivered'
    STATUS_CANCELED = 'Canceled'
    STATUS_CHOICES = (
        (STATUS_NEW, 'New'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_COMPILED, 'Compiled'),
        (STATUS_SHIPPED, 'Shipped'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CANCELED, 'Canceled')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Пользователь')
    dt = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES,
                              default=STATUS_NEW, max_length=50)

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
                                blank=True, verbose_name='Товар',
                                related_name='order_items')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Магазин')
    quantity = models.PositiveIntegerField(verbose_name='Количество',
                                           default=1)

    def __str__(self):
        return '{}_{}'.format(self.order, self.product)


# https://webdevblog.ru/modelirAovanie-polimorfizma-v-django/
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Phone(Contact):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Номер должен быть в формате: '+70000000'. Поддерживается до 15 цифр.")
    phone_num = models.CharField(validators=[phone_regex], max_length=17,
                             blank=True, verbose_name='Номер телефона')

    def __str__(self):
        return '{}'.format(self.phone_num)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'


class Address(Contact):
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    building = models.PositiveIntegerField(verbose_name='Дом')
    block = models.PositiveIntegerField(verbose_name='Корпус')
    apartment = models.PositiveIntegerField(verbose_name='Квартира')

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}, {self.block}, {self.apartment}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'





