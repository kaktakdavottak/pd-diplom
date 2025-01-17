from django.db import models
from django.conf import settings


class Shop(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=50)
    url = models.URLField(verbose_name='Ссылка')
    filename = models.FilePathField(verbose_name='Файл',
                                    path=settings.BASE_DIR)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

