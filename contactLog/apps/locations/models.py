from django.db import models


# Create your models here.
class Estado(models.Model):

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
    Nombre = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return self.Nombre


class Ciudad(models.Model):

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    Nombre = models.CharField("Nombre", max_length=50)
    Estado = models.ForeignKey(Estado)

    def __str__(self):
        return self.Nombre


class Sucursal(models.Model):

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    Street = models.CharField("Calle", max_length=45)
    Ciudad = models.ForeignKey(Ciudad)

    def __str__(self):
        return self.Street
