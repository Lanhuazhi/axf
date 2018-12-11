# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('trackid', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=150)),
                ('categoryid', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=150)),
                ('childcid1', models.CharField(max_length=20)),
                ('productid1', models.CharField(max_length=20)),
                ('longname1', models.CharField(max_length=25)),
                ('price1', models.CharField(max_length=10)),
                ('marketprice1', models.CharField(max_length=10)),
                ('img2', models.CharField(max_length=150)),
                ('childcid2', models.CharField(max_length=20)),
                ('productid2', models.CharField(max_length=20)),
                ('longname2', models.CharField(max_length=25)),
                ('price2', models.CharField(max_length=10)),
                ('marketprice2', models.CharField(max_length=10)),
                ('img3', models.CharField(max_length=150)),
                ('childcid3', models.CharField(max_length=20)),
                ('productid3', models.CharField(max_length=20)),
                ('longname3', models.CharField(max_length=25)),
                ('price3', models.CharField(max_length=10)),
                ('marketprice3', models.CharField(max_length=10)),
            ],
        ),
    ]
