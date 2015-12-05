# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('first_name', models.CharField(default=b'', max_length=30, verbose_name=b'first name')),
                ('last_name', models.CharField(default=b'', max_length=30)),
                ('number', models.CharField(default=b'', max_length=15)),
                ('email', models.EmailField(default=b'', max_length=75)),
                ('reason', models.TextField(default=b'')),
                ('order_id', models.CharField(primary_key=True, default=b'', serialize=False, editable=False, max_length=10, unique=True)),
                ('order_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
                ('experience', models.ForeignKey(verbose_name=b'Experience', to='experience.Experience')),
            ],
        ),
    ]
