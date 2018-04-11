# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-30 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATRitems', '0002_remove_item_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='question_text',
            new_name='meeting_no',
        ),
        migrations.AddField(
            model_name='item',
            name='agenda_item',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='agenda_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='decision_taken',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
