# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-13 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goservices',
            name='levels',
        ),
        migrations.RemoveField(
            model_name='goservices',
            name='port',
        ),
        migrations.AddField(
            model_name='goservices',
            name='level',
            field=models.CharField(max_length=128, null=True, verbose_name='level'),
        ),
        migrations.AddField(
            model_name='goservices',
            name='ports',
            field=models.CharField(max_length=128, null=True, verbose_name='ports'),
        ),
    ]
