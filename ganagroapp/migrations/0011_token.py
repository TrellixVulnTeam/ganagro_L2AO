# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ganagroapp', '0010_auto_20170623_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField()),
            ],
        ),
    ]