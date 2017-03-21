# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmetadata',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]
