# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_auto_20181124_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('productid', models.CharField(max_length=10)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=150)),
                ('productlongname', models.CharField(max_length=150)),
                ('isxf', models.CharField(max_length=10)),
                ('pmdesc', models.CharField(max_length=10)),
                ('specifics', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('marketprice', models.CharField(max_length=10)),
                ('categoryid', models.CharField(max_length=10)),
                ('childcid', models.CharField(max_length=10)),
                ('childcidname', models.CharField(max_length=50)),
                ('dealerid', models.CharField(max_length=10)),
                ('storenums', models.CharField(max_length=10)),
                ('productnum', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='market',
            name='childtypenames',
            field=models.TextField(max_length=100),
        ),
    ]
