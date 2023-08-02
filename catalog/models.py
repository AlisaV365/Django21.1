from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=350, unique=True, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=350, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(upload_to='media/catalog/', **NULLABLE)
    category = models.ForeignKey(Category, to_field='name', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_of_creation = models.DateField(max_length=10, verbose_name='дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')


    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)

    # user = models.ForeignKey(User, to_field='email', on_delete=models.CASCADE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name} ({self.category_id}) ({self.description})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=350, verbose_name='название версии')

    active_version = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.product} - {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
