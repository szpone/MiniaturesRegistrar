# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minis', '0006_miniature_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='number',
            field=models.IntegerField(choices=[(0, 'Skin'), (1, 'Weapon_wood'), (2, 'Eyes'), (3, 'Armor'), (4, 'Weapon_steel'), (5, 'Clothes_upper'), (6, 'Clothes_lower'), (7, 'Boots'), (8, 'Golden_elements'), (9, 'Bone_elements'), (10, 'Base')]),
        ),
    ]