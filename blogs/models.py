from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    images = models.ImageField(upload_to='home/images/', verbose_name='Фотографии')

    def __str__(self):
        return f'Фотография с id {self.id}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Employees(models.Model):
    images = models.ImageField(upload_to='employees/images/', verbose_name='Фотография сотрудника')
    name = models.CharField(max_length=150, verbose_name='Имя и Фамилия')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'Сотрудник {self.name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Biography(models.Model):
    images = models.ImageField(upload_to='biography/images/', verbose_name='Фотография')
    name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Биография'
        verbose_name_plural = 'Биографии'


class Blog(models.Model):
    images = models.ImageField(upload_to='blog/images/', verbose_name='Фото')
    title = models.CharField(max_length=250, verbose_name='Название')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

