# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_message_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='date',
        ),
    ]
