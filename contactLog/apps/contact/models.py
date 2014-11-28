# -*- coding: utf-8 -*-

from django.db import models

from apps.locations.models import Ciudad


# Model for Sucursales
class Sucursales(models.Model):
    street = models.CharField('Calle', max_length=45)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

    def __unicode__(self):
        return self.street


# Model for Contacts
class Contacts(models.Model):
    name = models.CharField('Nombre', max_length=45)
    street = models.CharField('Calle', max_length=45)
    num_ext = models.CharField('Número', max_length=5)
    colonia = models.CharField('Colonia', max_length=45)
    zip_code = models.PositiveSmallIntegerField('Código Postal', max_length=5)
    ciudad = models.ForeignKey(Ciudad)
    sucursales = models.ForeignKey(Sucursales)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __unicode__(self):
        return self.name
