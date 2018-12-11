# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0008_cartgoods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('times', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=200)),
                ('ordid', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=15)),
            ],
        ),
    ]
