# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20161113_1809'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
