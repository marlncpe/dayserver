# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from granjas.models import *
from website.models import *
# Create your models here.

class Patologias_grupo(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    descripcion = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Patologias(models.Model):
    casusa = models.CharField(max_length=255,blank=False)
    grupo = models.ForeignKey(Patologias_grupo)
    causa_muerte = models.CharField(max_length=50, blank=True)
    causa_descarte = models.CharField(max_length=50, blank=True) 
    causa_tratamiento = models.CharField(max_length=50, blank=True)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

class animales_genetica(models.Model):
    nombre = models.CharField(max_length=100,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class animale(models.Model):
    granja = models.ForeignKey(Granja)
    galpon = models.ForeignKey(Galpone)
    corrales = models.ForeignKey(Corrale)
    lote = models.CharField(max_length=255, blank=False)
    edad = models.CharField(max_length=3, blank=False)
    num_machos = models.CharField(max_length=12, blank=False)
    num_hembras = models.CharField(max_length=12 , blank=False)
    peso_total = models.CharField(max_length=16, blank=True)
    remision = models.CharField(max_length=255, blank=True)
    valor_lote = models.CharField(max_length=16, blank=False)
    procedencia = models.CharField(max_length=255, blank=False)
    genetica = models.ForeignKey(animales_genetica)
    observaciones = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(Status)

class mortalidad(models.Model):
    granja = models.ForeignKey(Granja)
    galpon = models.ForeignKey(Galpone)
    corral = models.ForeignKey(Corrale)
    fecha = models.CharField(max_length=10, blank=False)
    lote = models.CharField(max_length=255, blank=False)
    sexo = models.CharField(max_length=255, blank=False)
    causa = models.CharField(max_length=255, blank=False)
    cantidad = models.CharField(max_length=255, blank=False)
    peso = models.CharField(max_length=16, blank=True)
    destino = models.CharField(max_length=255, blank=True)
    
class Medicamentos_laboratorio(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    registro_comercial = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_tipo(models.Model):
    nombre = models.CharField(max_length=100,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    Laboratorio = models.ForeignKey(Medicamentos_laboratorio)
    registro_ica = models.CharField(max_length=255, blank=False)
    presentacion = models.CharField(max_length=255, blank=True)
    tipo = models.ForeignKey(Medicamentos_tipo)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_indicacione(models.Model):
    medicamento = models.ForeignKey(Medicamento)
    indicacion = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

class Traslados_animale(models.Model):
    granja = models.ForeignKey(Granja)
    lote_origen = models.CharField(max_length=255, blank=True)
    lote_destino = models.CharField(max_length=255, blank=True)
    nro_animales = models.CharField(max_length=255, blank=True)
    causa = models.CharField(max_length=255, blank=True)
    fecha = models.CharField(max_length=15, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Traslados_alimento(models.Model):
    granja = models.ForeignKey(Granja)
    origen = models.CharField(max_length=255, blank=True)
    destino = models.CharField(max_length=255, blank=True)
    referencia = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=16, blank=True)
    valor_flete = models.CharField(max_length=16, blank=True)

class Salidas_placebo(models.Model):
    granja = models.ForeignKey(Granja)
    galpon = models.ForeignKey(Galpone)
    corral = models.ForeignKey(Corrale)
    lote = models.CharField(max_length=255, blank=True)
    num_machos = models.CharField(max_length=255, blank=True)
    num_hembras = models.CharField(max_length=255, blank=True)
    peso_total = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    tipo_salida = models.CharField(max_length=255, blank=True)
    destino = models.CharField(max_length=255, blank=True)
    vehiculo = models.CharField(max_length=255, blank=True)
    cuarentena = models.CharField(max_length=255, blank=True)
    precio_total = models.CharField(max_length=255, blank=True)
    remision = models.CharField(max_length=255, blank=True)
    valor_flete = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Tratamientos(models.Model):
    granja = models.ForeignKey(Granja)
    Galpon = models.ForeignKey(Galpone)
    corral = models.ForeignKey(Corrale)
    causa = models.CharField(max_length=255, blank=True)
    lote = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    edad = models.CharField(max_length=255, blank=True)
    medicamento = models.CharField(max_length=255, blank=True)
    laboratorio = models.CharField(max_length=255, blank=True)
    lote_medicamento = models.CharField(max_length=255, blank=True)
    ICA = models.CharField(max_length=255, blank=True)
    dosis = models.CharField(max_length=255, blank=True)
    duracion = models.CharField(max_length=255, blank=True)
    retiro = models.CharField(max_length=255, blank=True)
    via_aplicacion = models.CharField(max_length=255, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    responsable = models.OneToOneField(settings.AUTH_USER_MODEL)
    fecha_registro = models.DateField(auto_now_add=True)