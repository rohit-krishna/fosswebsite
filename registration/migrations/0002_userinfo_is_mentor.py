# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_mentor',
            field=models.BooleanField(default=False),
        ),
    ]
