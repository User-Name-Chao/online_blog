# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-28 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selfboke',
            name='like_num',
        ),
        migrations.RemoveField(
            model_name='selfboke',
            name='talk_num',
        ),
    ]