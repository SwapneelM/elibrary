# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0007_auto_20160103_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='history',
            field=models.TextField(blank=True),
        ),
    ]
