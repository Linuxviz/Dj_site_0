# Generated by Django 3.1.4 on 2020-12-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='novelty',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='novelty',
            name='content',
            field=models.TextField(blank=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='novelty',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='novelty',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='novelty',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='novelty',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]
