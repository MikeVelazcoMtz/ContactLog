# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Estado(models.Model):

    class Meta:
        verbose_name = u"Estado"
        verbose_name_plural = u"Estados"
    Nombre = models.CharField(u"Nombre", max_length=50, unique=True)

    def __unicode__(self):
        return self.Nombre


class Ciudad(models.Model):

    class Meta:
        verbose_name = u"Ciudad"
        verbose_name_plural = u"Ciudades"

    Nombre = models.CharField(u"Nombre", max_length=50)
    Estado = models.ForeignKey(Estado)

    def __unicode__(self):
        return self.Nombre


class Sucursal(models.Model):

    class Meta:
        verbose_name = u"Sucursal"
        verbose_name_plural = u"Sucursales"

    Street = models.CharField(u"Calle", max_length=45)
    Ciudad = models.ForeignKey(Ciudad)

    def __unicode__(self):
        return self.Street
