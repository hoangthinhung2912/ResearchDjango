# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-16 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180716_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2018, 7, 16, 9, 41, 42, 291000, tzinfo=utc)),
        ),
    ]
