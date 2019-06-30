from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True, verbose_name='Пользователь')
    dt = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.BooleanField(verbose_name='Статус', default=False)


class OrderItem(models.Model):
    pass


class Contact(models.Model):
    pass

