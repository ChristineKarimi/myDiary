# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-17 11:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('your_story', tinymce.models.HTMLField()),
                ('contact', models.CharField(default='kim@gmail.com', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Bike riding', max_length=50)),
                ('diary_image', models.ImageField(default='city.jpeg', upload_to='hood/')),
                ('entries', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NeighborProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('prof_pic', models.ImageField(default='avatar.png', upload_to='profiles/')),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Neighborhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
