# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-08 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='context',
            field=models.TextField(max_length=300),
        ),
    ]