# Generated by Django 4.0.1 on 2022-02-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя')),
                ('name', models.CharField(default=' ', max_length=30, verbose_name='Имя пользователя')),
                ('project_name', models.CharField(max_length=50, null=True, verbose_name='Название проекта')),
                ('project_desc', models.CharField(max_length=10000, null=True, verbose_name='Описание проекта')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Проекты',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
