# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-30 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATRitems', '0003_auto_20180330_0030'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
