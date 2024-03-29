# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-04 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_userprofile_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='post',
        ),
        migrations.RemoveField(
            model_name='posttag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(blank=True, through='posts.UserProfileTag', to='posts.UserProfile'),
        ),
        migrations.DeleteModel(
            name='PostTag',
        ),
        migrations.AddField(
            model_name='userprofiletag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Tag'),
        ),
        migrations.AddField(
            model_name='userprofiletag',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tags',
            field=models.ManyToManyField(blank=True, through='posts.UserProfileTag', to='posts.Tag'),
        ),
    ]
