# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-05-07 10:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('no_of_songs', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=20)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]