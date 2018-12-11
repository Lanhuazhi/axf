# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_nav'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]
