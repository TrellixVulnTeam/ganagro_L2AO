# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ganagroapp', '0002_auto_20170603_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]