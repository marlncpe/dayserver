# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Granjas_tipo(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Granja(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    tipo_granja = models.ForeignKey(Granjas_tipo, null=True, blank=True)
    area = models.CharField(max_length=11, blank=False)
    ubicacion = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)
    dueno = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.nombre 

class Galpone(models.Model):
    granja = models.ForeignKey(Granja)
    nombre = models.CharField(max_length=255, blank=False)
    numero = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Corrale(models.Model):
    galpon = models.ForeignKey(Galpone)
    numero = models.CharField(max_length=255, blank=False)
    area_disponible = models.CharField(max_length=255, blank=False)
    capacidad = models.CharField(max_length=255, blank=False)#nro animales
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Inmunocastracione(models.Model):
    granja = models.ForeignKey(Granja)
    rastro = models.CharField(max_length=11,blank=True)
    periodo_venta = models.CharField(max_length=11,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Inmunocastraciones_extendida(models.Model):
    Inmunocastracion = models.ForeignKey(Inmunocastracione)
    numero = models.CharField(max_length=50,blank=False)
    fecha_aplicacion = models.CharField(max_length=10,blank=True) 
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre