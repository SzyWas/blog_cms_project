# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 23:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0004_auto_20161002_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=1000)),
                ('author', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.PostEntry')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': ['Comments'],
            },
        ),
    ]
