# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20141128_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='colonia',
            field=models.CharField(max_length=45, verbose_name=b'Colonia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='num_ext',
            field=models.CharField(max_length=5, verbose_name=b'N\xc3\xbamero'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='street',
            field=models.CharField(max_length=45, verbose_name=b'Calle'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='sucursales',
            field=models.ForeignKey(to='locations.Sucursal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='zip_code',
            field=models.PositiveSmallIntegerField(max_length=5, verbose_name=b'C\xc3\xb3digo Postal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sucursales',
            name='street',
            field=models.CharField(max_length=45, verbose_name=b'Calle'),
            preserve_default=True,
        ),
    ]
