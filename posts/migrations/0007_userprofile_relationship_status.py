# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 03:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20160304_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='relationship_status',
            field=models.CharField(choices=[('S', 'Single'), ('E', 'Engaged'), ('M', 'Married'), ('I', 'In a relationship')], default=datetime.datetime(2016, 3, 4, 3, 53, 51, 574618, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
