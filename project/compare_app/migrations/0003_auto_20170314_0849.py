# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare_app', '0002_auto_20170314_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmetadata',
            name='key_words',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='productmetadata',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
