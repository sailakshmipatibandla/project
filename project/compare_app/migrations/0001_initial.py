# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=1000)),
                ('site', models.CharField(default=b'ebay', max_length=10, choices=[(b'ebay', b'EBay'), (b'amazon', b'Amazon'), (b'snapdeal', b'Snapdeal'), (b'paytm', b'PayTM')])),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('key_words', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('rating', models.DecimalField(max_digits=5, decimal_places=2)),
                ('latest', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='compare_app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='compare_app.Category')),
            ],
        ),
        migrations.AddField(
            model_name='productmetadata',
            name='sub_catagory',
            field=models.ForeignKey(to='compare_app.SubCategory'),
        ),
    ]
