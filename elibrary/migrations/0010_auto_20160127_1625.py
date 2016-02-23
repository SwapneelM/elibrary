# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0009_auto_20160106_0153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
        migrations.AddField(
            model_name='book',
            name='publication',
            field=models.CharField(max_length=200, default=' '),
        ),
    ]
