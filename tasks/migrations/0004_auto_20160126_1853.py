# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_category_selected'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('choice_selected', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_title', models.CharField(max_length=50)),
                ('question_text', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='tasks.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='tasks.Question'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='category',
            old_name='selected',
            new_name='category_selected',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='cat_title',
            new_name='category_title',
        ),
    ]
