# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0005_market'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='childtypenames',
            field=models.CharField(max_length=100),
        ),
    ]
