# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-04 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='about',
            field=models.TextField(default='-'),
        ),
    ]
