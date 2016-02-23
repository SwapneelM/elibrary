# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0008_userprofile_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='area',
            field=models.CharField(default=' ', max_length=400),
        ),
        migrations.AddField(
            model_name='book',
            name='libID',
            field=models.CharField(default=' ', max_length=400),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.CharField(default=' ', max_length=400),
        ),
    ]
