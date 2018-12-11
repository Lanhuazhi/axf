# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_auto_20181125_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartGoods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('userid', models.CharField(max_length=15)),
                ('productid', models.CharField(max_length=11)),
                ('goodsnumber', models.IntegerField()),
                ('price', models.IntegerField()),
                ('is_select', models.BooleanField(default=True)),
                ('productimg', models.CharField(max_length=150)),
                ('productname', models.CharField(max_length=150)),
                ('orderid', models.CharField(max_length=20,default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
