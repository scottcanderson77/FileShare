# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0009_auto_20161130_0122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='uploaded_at',
        ),
    ]
