# Generated by Django 2.0.5 on 2019-06-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('filename', models.FilePathField(path='/home/semen/git_projects/pd-diplom/orders', verbose_name='Файл')),
            ],
        ),
    ]