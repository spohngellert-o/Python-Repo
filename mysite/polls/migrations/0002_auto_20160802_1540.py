# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'permissions': ('can_vote', 'Whether a user can vote or not on polls.')},
        ),
    ]
