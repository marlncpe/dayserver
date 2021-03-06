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
    area = models.CharField(max_length=11, blank=False)
    numero = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)
    dueno = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    def __unicode__(self):
        return self.nombre

class Corrale(models.Model):
    galpon = models.ForeignKey(Galpone)
    numero = models.CharField(max_length=255, blank=False)
    area_disponible = models.CharField(max_length=255, blank=False)
    capacidad = models.CharField(max_length=255, blank=False)#nro animales
    fecha_registro = models.DateField(auto_now_add=True)
    dueno = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return self.numero

class Inmunocastracione(models.Model):
    granja = models.ForeignKey(Granja)
    rastro = models.CharField(max_length=11,blank=True)
    pdosis = models.CharField(max_length=11,blank=False)
    sdosis = models.CharField(max_length=11,blank=True)
    tdosis = models.CharField(max_length=11, blank=True)
    periodo_venta = models.CharField(max_length=11,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.rastro

class animales_admin(models.Model):
    cantidad = models.CharField(max_length=11,blank=True)
    granja = models.ForeignKey(Granja)
    dueno = models.ForeignKey(settings.AUTH_USER_MODEL)
    #encargado_asignacion = models.ForeignKey(settings.AUTH_USER_MODEL)
    fecha_registro = models.DateField(auto_now_add=True)

    
