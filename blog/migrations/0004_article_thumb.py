# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-05 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180702_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='缩略图'),
        ),
    ]