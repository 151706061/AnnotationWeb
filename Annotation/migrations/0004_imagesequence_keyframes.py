# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0003_auto_20160601_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(max_length=1024)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='KeyFrames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_nr', models.PositiveIntegerField()),
                ('image_sequence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.ImageSequence')),
            ],
        ),
    ]
