# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-04 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20200104_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='poll',
            name='ln',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='poll',
            name='yt',
            field=models.TextField(default='-'),
        ),
    ]
