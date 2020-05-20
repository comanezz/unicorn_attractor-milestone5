# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-20 23:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0011_auto_20200520_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_bug', to=settings.AUTH_USER_MODEL),
        ),
    ]
