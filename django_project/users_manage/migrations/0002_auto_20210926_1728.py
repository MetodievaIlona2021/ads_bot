# Generated by Django 3.2.7 on 2021-09-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Название видео')),
                ('description', models.TextField(max_length=1000, null=True, verbose_name='Описание к видео')),
                ('thumb_url', models.CharField(max_length=100, null=True, verbose_name='Превью к видео')),
                ('url', models.CharField(max_length=100, null=True, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.AlterField(
            model_name='articles',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
