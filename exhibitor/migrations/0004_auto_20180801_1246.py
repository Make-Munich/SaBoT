# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 13:22
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitor', '0003_exhibitor_form_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitor',
            name='boothArea',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, b'3D Printing'), (2, b'Arduino'), (3, b'Art'), (4, b'Biohacking'), (5, b'Bionics'), (6, b'Crafts'), (7, b'Design'), (8, b'Digital Fabrication'), (9, b'Education'), (10, b'Electronics'), (11, b'Fashion'), (12, b'Food & Agriculture'), (13, b'Garden'), (14, b'Healthcare'), (15, b'Home Automation'), (16, b'Interaction'), (17, b'Internet of Things'), (18, b'Model Making'), (19, b'New Materials'), (20, b'Raspberry Pi'), (21,
                b'Robot & Drones'), (22, b'Science'), (23, b'Social design'), (24, b'Sustainability'), (25, b'Startup / Small Business'), (26, b'Tiny Houses'), (27, b'Transportation'), (28, b'Wearables'), (29, b'Wellness'), (30, b'Young Makers'), (31, b'Other')], max_length=3, max_choices=3, verbose_name='Which area is your booth in?'),
        ),
        migrations.AlterField(
            model_name='exhibitor',
            name='boothPreferedLocation',
            field=models.PositiveIntegerField(choices=[(1, b'Main Floor'), (2, b'Stage'), (0, b'No preference')], default=0, verbose_name='Do you have a preferred location for your booth?'),
        ),
    ]
