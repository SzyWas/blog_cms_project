# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-12 00:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Comments'},
        ),
    ]
