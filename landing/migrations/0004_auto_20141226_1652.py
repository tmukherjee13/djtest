# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_cms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms',
            name='facebook',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cms',
            name='gplus',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cms',
            name='linkedin',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cms',
            name='twitter',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
