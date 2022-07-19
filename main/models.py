from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Projects(models.Model):
    user_id = models.IntegerField(verbose_name='ID пользователя')
    user_name = models.CharField(max_length=30, verbose_name='Имя пользователя', default=" ")
    project_name = models.CharField(max_length=50,verbose_name='Название проекта', null=True)
    project_desc = models.CharField(max_length=500,verbose_name='Описание проекта', null=True)
    project_full_desc = models.CharField(max_length=10000,verbose_name='Полное описание проекта', null=True)
    price = models.IntegerField(verbose_name='Цена')
    active = models.CharField(max_length=10, verbose_name='Активна', null=True)


    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return str(f"{self.project_name}")


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    service_type = models.CharField(max_length=50, null=True)
    vk = models.CharField(max_length=250, null=True)
    ok = models.CharField(max_length=250, null=True)
    fb = models.CharField(max_length=250, null=True)
    insta = models.CharField(max_length=250, null=True)
    twitter = models.CharField(max_length=250, null=True)
    viber = models.CharField(max_length=250, null=True)
    whatsapp = models.CharField(max_length=250, null=True)


    def __str__(self):
        return self.user.username
