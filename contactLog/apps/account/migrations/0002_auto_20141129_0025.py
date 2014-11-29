# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='calle',
            field=models.CharField(max_length=45, verbose_name=b'Calle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='colonia',
            field=models.CharField(max_length=45, verbose_name=b'Colonia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='num_ext',
            field=models.CharField(max_length=45, verbose_name=b'N\xc3\xbamero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=45, verbose_name=b'Tel\xc3\xa9fono'),
            preserve_default=True,
        ),
    ]
