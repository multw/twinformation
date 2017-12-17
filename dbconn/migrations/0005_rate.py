# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 10:33
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbconn', '0004_auto_20171119_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=40)),
                ('jsondata', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
