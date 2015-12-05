# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('name', models.CharField(default=b'', max_length=50)),
                ('location', models.CharField(default=b'', max_length=50)),
                ('number', models.CharField(default=b'', max_length=15)),
                ('email', models.EmailField(default=b'', max_length=75)),
                ('description', models.TextField(default=b'')),
                ('photo', models.CharField(default=b'', max_length=250)),
                ('experience_id', models.CharField(primary_key=True, default=b'', serialize=False, editable=False, max_length=10, unique=True)),
                ('creation_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
        ),
    ]
