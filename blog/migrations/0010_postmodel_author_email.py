# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-16 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180716_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
