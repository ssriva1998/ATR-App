# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-05 01:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATRitems', '0008_auto_20180405_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='functionaries',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
