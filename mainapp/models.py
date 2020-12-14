from django.db import models


# Create your models here.

class Novelty(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateField(auto_now_add=True,
                                  verbose_name='Дата создания')  # auto_now_add - один раз сохраняет время
    updated_at = models.DateField(auto_now=True, verbose_name='Дата изменения')  # Каждый раз при изменении
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True,
                                 verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'  # Название в админке для всей модели
        verbose_name_plural = 'Новости'  # Во множественном числе
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=120, db_index=True, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'  # Название в админке для всей модели
        verbose_name_plural = 'Категории'  # Во множественном числе
        ordering = ['title']

    def __str__(self):
        return self.title
