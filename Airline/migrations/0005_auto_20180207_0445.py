# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-07 04:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Airline', '0004_auto_20180207_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='passengers',
        ),
        migrations.DeleteModel(
            name='UserAge',
        ),
    ]