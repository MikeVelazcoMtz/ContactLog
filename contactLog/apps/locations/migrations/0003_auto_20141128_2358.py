# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='Nombre',
            field=models.CharField(unique=True, max_length=50, verbose_name='Nombre'),
            preserve_default=True,
        ),
    ]
