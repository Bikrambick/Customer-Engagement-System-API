# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20170928_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='farebase_ui',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lat',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lng',
            field=models.IntegerField(null=True),
        ),
    ]