# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-09 02:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('channel', 'name', 'parent')]),
        ),
    ]
