# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoDoApp', '0007_auto_20160523_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubinformation',
            name='branch_sha',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
