# Generated by Django 4.0.3 on 2022-04-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_account_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='fb',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='insta',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='ok',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='twitter',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='viber',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='vk',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='whatsapp',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
