# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import sabot.utils


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0026_auto_20170116_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoring',
            name='logo',
            field=models.ImageField(blank=True, upload_to=sabot.utils.upload_transform_func, verbose_name='Company logo for homepage (preferably as PNG)'),
        ),
        migrations.AlterField(
            model_name='sponsoring',
            name='programAd',
            field=models.FileField(blank=True, upload_to=sabot.utils.upload_transform_func, verbose_name='PDF of your advertisement in our printed program'),
        ),
        migrations.AlterField(
            model_name='sponsoring',
            name='vectorLogo',
            field=models.FileField(blank=True, upload_to=sabot.utils.upload_transform_func, verbose_name='Company logo as vector graphics (preferably PDF or SVG) for printed advertisements such as posters, flyers and visitor badges'),
        ),
    ]
