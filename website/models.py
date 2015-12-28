# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from granjas.models import *
# Create your models here.
class Status(models.Model):
    nombre = models.CharField(max_length=11,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Usuarios_permiso(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nacionalidad=models.CharField(max_length=2,blank=True)
    cedula=models.CharField(max_length=21,blank=True)
    direccion=models.CharField(max_length=250,blank=True)
    telefono=models.CharField(max_length=12,blank=True)
    foto=models.ImageField(upload_to='foto_perfil',blank=True)
    tipo_permiso= models.ForeignKey(Usuarios_permiso)
    respuesta_seguridad= models.CharField(max_length=60,blank=True)
    persona_contacto = models.CharField(max_length=255, blank=True)
    dias_pago = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(Status)
'''
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
   # granja = models.ForeignKey(Granja)
    nombre = models.CharField(max_length=255, blank=False)
    numero = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

class Corrale(models.Model):
    #galpon = models.ForeignKey(Galpone)
    numero = models.CharField(max_length=255, blank=False)
    area_disponible = models.CharField(max_length=255, blank=False)
    capacidad = models.CharField(max_length=255, blank=False)#nro animales
    fecha_registro = models.DateField(auto_now_add=True)

class Inmunocastracione(models.Model):
    granja = models.ForeignKey(Granja)
    rastro = models.CharField(max_length=11,blank=True)
    periodo_venta = models.CharField(max_length=11,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Inmunocastraciones_extendida(models.Model):
    Inmunocastracion = models.ForeignKey(Inmunocastracione)
    numero = models.CharField(max_length=50,blank=False)
    fecha_aplicacion = models.CharField(max_length=10,blank=True) 
    fecha_registro = models.DateField(auto_now_add=True)
'''
class Alimentos_fabrica(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimentos_fase(models.Model):
    nombre = models.CharField(max_length=50,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimentos_tipo(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimento(models.Model):
    fabrica = models.ForeignKey(Alimentos_fabrica)
    fase = models.ForeignKey(Alimentos_fase)
    nombre = models.CharField(max_length=255, blank=False)
    presentacion = models.CharField(max_length=255,blank=True)
    kg_bulto = models.CharField(max_length=11,blank=False)
    tipo_alimento = models.ForeignKey(Alimentos_tipo)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

class Mano_obras_tipo(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Mano_obra(models.Model):
    granja = models.ForeignKey(Granja)
    fecha_inicial = models.DateField(auto_now_add=False)
    fecha_final = models.DateField(auto_now_add=False)
    tipo = models.ForeignKey(Mano_obras_tipo)
    detalle = models.CharField(max_length=255,blank=True)
    num_personas_pagadas = models.CharField(max_length=11, blank=False)
    valor_total = models.CharField(max_length=11 ,blank=False)

class personal(models.Model):#pendiente con esta tabla me parece q es redundante
    nombres = models.CharField(max_length=60, blank=False)
    apellidos = models.CharField(max_length=60, blank=False)
    siglas = models.CharField(max_length=4, blank=True)
    centro_costo = models.CharField(max_length=255, blank=True)
    fecha_ingreso = models.CharField(max_length=10, blank=False)
    fecha_retiro = models.CharField(max_length=10, blank=True)
    status = models.ForeignKey(Status)
    eps = models.CharField(max_length=255, blank=True)
    contacto = models.CharField(max_length=16, blank=True)

class Insumo(models.Model):
    descripcion = models.CharField(max_length=255, blank=False)
    Marca = models.CharField(max_length=50, blank=True)
    presentacion = models.CharField(max_length=50, blank=True)
    unidades_paquetes = models.CharField(max_length=11, blank=False)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

class Pedidos_tipo(models.Model):
    nombre = models.CharField(max_length=10,blank=False)
    descripcion = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Pedido(models.Model):
    granja = models.ForeignKey(Granja)
    tipo = models.ForeignKey(Pedidos_tipo)
    fecha = models.CharField(max_length=10, blank=False)
    subtotal = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class pedidos_medicamentos_extendido(models.Model):
    pedido = models.ForeignKey(Pedido)
    producto = models.CharField(max_length=255,blank=False)
    Cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class pedidos_alimentos_extendido(models.Model):
    pedido = models.ForeignKey(Pedido)
    referencia = models.CharField(max_length=255,blank=True)
    medicado = models.CharField(max_length=255, blank=True)
    dosis = models.CharField(max_length=15, blank=True)
    fecha_recogida = models.CharField(max_length=10, blank=False)
    observaciones = models.CharField(max_length=255, blank=True)
    valor = models.CharField(max_length=12, blank=False)


class Compras_tipo(models.Model):
    nombre = models.CharField(max_length=10,blank=False)
    descripcion = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Compra(models.Model):
    granja = models.ForeignKey(Granja)
    tipo = models.ForeignKey(Pedidos_tipo)
    fecha = models.CharField(max_length=10, blank=False)
    subtotal = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Compras_insumo(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.CharField(max_length=255,blank=False)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class Compras_medicamento(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.CharField(max_length=255,blank=False)
    lote = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class Compras_alimento(models.Model):
    compra = models.ForeignKey(Compra)
    referencia = models.CharField(max_length=255,blank=True)
    lote = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)
    medicado = models.CharField(max_length=255,blank=True)
    dosis_medicado = models.CharField(max_length=12, blank=True)
    valor_medicado = models.CharField(max_length=12, blank=True)

class Medicado(models.Model):
    producto = models.CharField(max_length=255, blank=True)
    Principio = models.CharField(max_length=255, blank=True)
    referencia = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)


class ventas(models.Model):
    lote = models.CharField(max_length=255, blank=True)
    num_machos = models.CharField(max_length=16, blank=True)
    num_hembras = models.CharField(max_length=16, blank=True)
    tipo = models.CharField(max_length=255, blank=True)
    peso = models.CharField(max_length=16, blank=True)
    cliente = models.OneToOneField(settings.AUTH_USER_MODEL)
    planta_sacrificio = models.CharField(max_length=255, blank=True)
    vehiculo = models.CharField(max_length=255, blank=True)
    cuarentena = models.CharField(max_length=255, blank=True)
    precio_total = models.CharField(max_length=255, blank=True)
    remision = models.CharField(max_length=255, blank=True)
    costos_flete = models.CharField(max_length=255, blank=True)
    pago = models.ForeignKey(Status)
    fecha_registro = models.DateField(auto_now_add=True)

class Costos_gasto(models.Model):
    granja = models.ForeignKey(Granja)
    Galpon = models.ForeignKey(Galpone)
    lote = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    amortizacion = models.CharField(max_length=255, blank=True)
    costos = models.CharField(max_length=255, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumos_tipo(models.Model):
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumo(models.Model):
    granja = models.ForeignKey(Granja)
    tipo = models.ForeignKey(Consumos_tipo)
    lote = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumos_farmaco(models.Model):
    consumo = models.ForeignKey(Consumo)
    producto = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Consumos_alimento(models.Model):
    consumo = models.ForeignKey(Consumo)
    referencia = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Consumos_insumo(models.Model):
    consumo = models.ForeignKey(Consumo)
    producto = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Curvas_crecimiento(models.Model):
    curva = models.CharField(max_length=255, blank=True)
    edad = models.CharField(max_length=255, blank=True)
    peso = models.CharField(max_length=255, blank=True)
    consumo = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Metas_pc(models.Model):
    granja = models.ForeignKey(Granja)
    etapa = models.CharField(max_length=255, blank=True)
    peso_inicial = models.CharField(max_length=255, blank=True)
    edad_inicial= models.CharField(max_length=255, blank=True)
    peso_final = models.CharField(max_length=255, blank=True)
    mortalidad = models.CharField(max_length=255, blank=True)
    conversion = models.CharField(max_length=255, blank=True)
    ganacia_peso = models.CharField(max_length=255, blank=True)
    gdp = models.CharField(max_length=255, blank=True)
    densidad = models.CharField(max_length=255, blank=True)
    dias_permanencia = models.CharField(max_length=255, blank=True)
    consumo_total = models.CharField(max_length=255, blank=True)
    consumo_animal_diario = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Metas_ceba(models.Model):
    granja = models.ForeignKey(Granja)
    peso_inicial = models.CharField(max_length=255, blank=True)
    edad_inicial = models.CharField(max_length=255, blank=True)
    peso_final = models.CharField(max_length=255, blank=True)
    mortalidad = models.CharField(max_length=255, blank=True)
    descarte = models.CharField(max_length=255, blank=True)
    conversion = models.CharField(max_length=255, blank=True)
    ganacia_peso = models.CharField(max_length=255, blank=True)
    gdp = models.CharField(max_length=255, blank=True)
    densidad = models.CharField(max_length=255, blank=True)
    dias_permanencia = models.CharField(max_length=255, blank=True)
    consumo_total = models.CharField(max_length=255, blank=True)
    consumo_animal_diario = models.CharField(max_length=255, blank=True)
    costos_produccion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Metas_destete_finalizacione(models.Model):
    granja = models.ForeignKey(Granja)
    peso_inicial = models.CharField(max_length=255, blank=True)
    edad_inicial = models.CharField(max_length=255, blank=True)
    peso_final = models.CharField(max_length=255, blank=True)
    mortalidad = models.CharField(max_length=255, blank=True)
    descarte = models.CharField(max_length=255, blank=True)
    conversion = models.CharField(max_length=255, blank=True)
    ganacia_peso = models.CharField(max_length=255, blank=True)
    gdp = models.CharField(max_length=255, blank=True)
    densidad = models.CharField(max_length=255, blank=True)
    dias_permanencia = models.CharField(max_length=255, blank=True)
    consumo_total = models.CharField(max_length=255, blank=True)
    consumo_animal_diario = models.CharField(max_length=255, blank=True)
    costos_produccion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Recordatorio(models.Model):
    tipo = models.CharField(max_length=50, blank=True)
    fecha_recordatorio = models.DateField()
    fecha_registro = models.DateField(auto_now_add=True)

class Recordatorios_extendido(models.Model):
    nombre = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    
'''

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

class Traslados_alimento(models.Model):
    granja = models.ForeignKey(Granja)
    origen = models.CharField(max_length=255, blank=True)
    destino = models.CharField(max_length=255, blank=True)
    referencia = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=16, blank=True)
    valor_flete = models.CharField(max_length=16, blank=True)

class Salidas_placebo(models.Model):
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
'''