# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0004_imagesequence_keyframes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KeyFrames',
            new_name='KeyFrame',
        ),
    ]
