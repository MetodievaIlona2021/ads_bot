from django.db import models
from sqlalchemy import sql


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimedBaseModel):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name='ID Пользователя Телеграм', unique=True, default=1)

    name = models.CharField(verbose_name='Имя пользователя', max_length=100)
    username = models.CharField(verbose_name='Username Телеграм', max_length=100, null=True)
    email = models.CharField(verbose_name='Email', max_length=100, null=True)

    def __str__(self):
        return f'№{self.id} ({self.user_id}) - {self.name}'


class Articles(TimedBaseModel):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название статьи', max_length=50)
    text = models.TextField(verbose_name='Текст статьи', max_length=5000, null=True)

    def __str__(self):
        return f'№{self.id} - от {self.name}'


class Videos(TimedBaseModel):
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Название видео', max_length=100)
    description = models.TextField(verbose_name='Описание к видео', max_length=1000, null=True)
    thumb_url = models.CharField(verbose_name='Превью к видео', max_length=100, null=True)
    url = models.CharField(verbose_name='Ссылка на видео', max_length=100, null=True)

    def __str__(self):
        return f'№{self.id} - от {self.name}'
