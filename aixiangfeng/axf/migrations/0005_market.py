# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0004_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('typeid', models.CharField(max_length=10)),
                ('typename', models.CharField(max_length=10)),
                ('childtypenames', models.CharField(max_length=10)),
                ('typesort', models.CharField(max_length=10)),
            ],
        ),
    ]
