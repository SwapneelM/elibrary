# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='SapID',
            field=models.IntegerField(default=60000000000),
        ),
    ]
