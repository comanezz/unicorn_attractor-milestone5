# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-09 20:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20200608_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='feature',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
