# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitor', '0002_exhibitor_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='boothPower',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Do you need power? (How many kwH)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='boothArea',
            field=models.PositiveIntegerField(choices=[(1, b'Electronics'), (2, b'3D Printing'), (0, b'No preference')], default=0, verbose_name='Which area is your booth in?'),
            preserve_default=False,
        ),
    ]