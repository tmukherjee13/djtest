# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20141225_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
                ('about_me', models.TextField()),
                ('facebook', models.CharField(max_length=20)),
                ('twitter', models.CharField(max_length=20)),
                ('gplus', models.CharField(max_length=20)),
                ('linkedin', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
