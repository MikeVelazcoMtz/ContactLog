# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_sucursal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('street', models.CharField(max_length=45)),
                ('num_ext', models.CharField(max_length=5)),
                ('colonia', models.CharField(max_length=45)),
                ('zip_code', models.PositiveSmallIntegerField(max_length=5)),
                ('ciudad', models.ForeignKey(to='locations.Ciudad')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=45)),
                ('ciudad', models.ForeignKey(to='locations.Ciudad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contacts',
            name='sucursales',
            field=models.ForeignKey(to='contact.Sucursales'),
            preserve_default=True,
        ),
    ]
