# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 11:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateField(auto_now_add=True)),
                ('modifyDate', models.DateField(auto_now=True)),
                ('projectName', models.CharField(max_length=128, verbose_name='Project name')),
                ('logo', models.ImageField(blank=True, upload_to=b'projects/logos', verbose_name='Project logo')),
                ('homepage', models.URLField(blank=True, verbose_name='Project homepage url')),
                ('descriptionDE', models.TextField(blank=True, verbose_name='Description text of your project (German)')),
                ('descriptionEN', models.TextField(blank=True, verbose_name='Description text of your project (English)')),
                ('boothPreferedLocation', models.PositiveIntegerField(choices=[(1, b'Main Floor'), (2, b'Stage'), (0, b'No preference')], default=0, verbose_name='Do you have a preferred location for your booth?')),
                ('boothNumTables', models.PositiveIntegerField(blank=True, null=True, verbose_name='How many tables do you need (roughly 1.20m x 0.80m)?')),
                ('boothNumChairs', models.PositiveIntegerField(blank=True, null=True, verbose_name='How many chairs do you need?')),
                ('boothPower', models.PositiveIntegerField(blank=True, null=True, verbose_name='Do you need power? (How many kwH)')),
                ('boothArea', multiselectfield.db.fields.MultiSelectField(choices=[(1, b'3D Printing'), (2, b'Arduino'), (3, b'Art'), (4, b'Biohacking'), (5, b'Bionics'), (6, b'Crafts'), (7, b'Design'), (8, b'Digital Fabrication'), (9, b'Education'), (10, b'Electronics'), (11, b'Fashion'), (12, b'Food & Agriculture'), (13, b'Garden'), (14, b'Healthcare'), (15, b'Home Automation'), (16, b'Interaction'), (17, b'Internet of Things'), (18, b'Model Making'), (19, b'New Materials'), (20, b'Raspberry Pi'), (21, b'Robot & Drones'), (22, b'Science'), (23, b'Social design'), (24, b'Sustainability'), (25, b'Startup / Small Business'), (26, b'Tiny Houses'), (27, b'Transportation'), (28, b'Wearables'), (29, b'Wellness'), (30, b'Young Makers'), (31, b'Other')], max_length=3, verbose_name='Which area is your booth in?')),
                ('boothComment', models.TextField(blank=True, verbose_name='Here you have the chance to leave us further comments regarding your booth:')),
                ('talkComment', models.TextField(blank=True, verbose_name='Here you have the chance to leave us further comments regarding your booth:')),
                ('workshopComment', models.TextField(blank=True, verbose_name='Here you have the chance to leave us further comments regarding your booth:')),
                ('accepted', models.BooleanField(default=False, editable=False)),
                ('year', models.PositiveIntegerField(editable=False, verbose_name='Conference year this project belongs to')),
                ('owner', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectParticipants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAdmin', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='participants',
            field=models.ManyToManyField(blank=True, editable=False, related_name='projectparticipation', through='project.ProjectParticipants', to=settings.AUTH_USER_MODEL),
        ),
    ]