# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minis', '0002_add_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='paint',
        ),
        migrations.RemoveField(
            model_name='paint',
            name='miniature',
        ),
        migrations.AddField(
            model_name='element',
            name='paints',
            field=models.ManyToManyField(to='minis.Paint'),
        ),
        migrations.AddField(
            model_name='miniature',
            name='paint',
            field=models.ManyToManyField(to='minis.Paint'),
        ),
    ]