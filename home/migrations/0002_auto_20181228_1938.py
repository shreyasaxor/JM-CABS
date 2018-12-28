# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-28 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='destination',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='pickup_time',
            field=models.DateTimeField(null=True),
        ),
    ]
