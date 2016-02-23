# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0010_auto_20160127_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copies',
            field=models.IntegerField(default=1),
        ),
    ]
