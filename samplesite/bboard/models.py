from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Рецепт')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    calories = models.FloatField(null=True, blank=True, verbose_name='Колории')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опублековано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')


class Meta:
    verbose_name_plural = 'Рецепты'
    verbose_name = 'Рецепт'
    ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name


class Meta:
    verbose_name_plural = 'Рубрики'


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
