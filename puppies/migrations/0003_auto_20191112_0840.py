# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-12 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('puppies', '0002_auto_20191112_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puppy',
            old_name='breed1',
            new_name='breed',
        ),
    ]