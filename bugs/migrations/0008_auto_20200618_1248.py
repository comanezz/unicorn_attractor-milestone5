# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-18 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_auto_20200617_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bug',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bugs.Bug'),
        ),
    ]
