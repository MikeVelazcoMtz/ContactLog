# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from apps.locations.models import Ciudad


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField('Teléfono', max_length=45)
    calle = models.CharField('Calle', max_length=45)
    num_ext = models.CharField('Número', max_length=45)
    colonia = models.CharField('Colonia', max_length=45)
    ciudad = models.ForeignKey(Ciudad)

    class Meta:
        verbose_name = 'Perfil de Usuario'
        verbose_name_plural = 'Perfiles de Usuarios'

    def __unicode__(self):
        return self.user.username