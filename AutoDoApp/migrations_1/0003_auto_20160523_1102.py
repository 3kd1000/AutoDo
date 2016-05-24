# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoDoApp', '0002_auto_20160520_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='githubinformation',
            name='user_email',
        ),
    ]
