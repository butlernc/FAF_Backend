# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=55)),
                ('long', models.DecimalField(max_digits=25, decimal_places=25)),
                ('lat', models.DecimalField(max_digits=25, decimal_places=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('isFBUser', models.BinaryField()),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=55)),
            ],
        ),
    ]
