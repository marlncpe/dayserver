# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class status(models.Model):
    nombre = models.CharField(max_length=11,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Usuarios_permiso(models.Model):
    nombre = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Usuario(User):
    User.add_to_class('nacionalidad', models.CharField(max_length=2,blank=True))
    User.add_to_class('cedula', models.CharField(max_length=21,blank=True))
    User.add_to_class('direccion', models.CharField(max_length=250,blank=True))
    User.add_to_class('telefono', models.CharField(max_length=12,blank=True))
    User.add_to_class('foto',models.ImageField(upload_to='foto_perfil',blank=True))
    User.add_to_class('tipo_permiso', models.ForeignKey(Usuarios_permiso))
    User.add_to_class('respuesta_seguridad', models.CharField(max_length=60,blank=True))

class Granjas_tipo(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Granja(models.Model):
    nombre = models.CharField(max_length=255, blank=False)
    tipo_granja = models.ForeignKey(Granjas_tipo)
    area = models.CharField(max_length=11, blank=False)
    ubicacion = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre 

class Galpone(models.Model):
    granja = models.ForeignKey(Granja)
    nombre = models.CharField(max_length=255, blank=False)
    numero = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

class Corrale(models.Model):
    galpon = models.ForeignKey(Galpone)
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

class Alimentos_fabrica(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    status = models.ForeignKey(status)
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
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class patologias_grupo(models.Model):
    nombre = models.CharField(max_length=255,blank=False)
    descripcion = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class patologias(models.Model):
    casusa = models.CharField(max_length=255,blank=False)
    grupo = models.ForeignKey(patologias_grupo)
    causa_muerte = models.CharField(max_length=50, blank=True)
    causa_descarte = models.CharField(max_length=50, blank=True) 
    causa_tratamiento = models.CharField(max_length=50, blank=True)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

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
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_indicacione(models.Model):
    medicamento = models.ForeignKey(Medicamento)
    indicacion = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=False)
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
    status = models.ForeignKey(status)
    eps = models.CharField(max_length=255, blank=True)
    contacto = models.CharField(max_length=16, blank=True)

class Insumo(models.Model):
    descripcion = models.CharField(max_length=255, blank=False)
    Marca = models.CharField(max_length=50, blank=True)
    presentacion = models.CharField(max_length=50, blank=True)
    unidades_paquetes = models.CharField(max_length=11, blank=False)
    status = models.ForeignKey(status)
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
    status = models.ForeignKey(status)

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


'''
CREATE TABLE `15 Compra Medicamentos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Producto` VARCHAR(255),
    `Cantidad` INTEGER,
    `Lote Fabricación` VARCHAR(255),
    `Fecha Vencimiento` DATETIME,
    `Retiro` INTEGER,
    `Valor` DOUBLE
) CHARACTER SET 'UTF8';

CREATE TABLE `16 Compra Alimento` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Referencia` VARCHAR(255),
    `Cantidad` INTEGER,
    `Lote Fabricación` VARCHAR(255),
    `Valor Alimento` DOUBLE,
    `Valor Total Flete` DOUBLE,
    `Medicado` VARCHAR(255),
    `Dosis Medicado (g/ton)` INTEGER,
    `Valor Medicado` DOUBLE
) CHARACTER SET 'UTF8';

CREATE TABLE `17 Medicados` (
    `Id` INTEGER PRIMARY KEY,
    `Producto` VARCHAR(255),
    `Principio Activo` VARCHAR(255),
    `Refencia` VARCHAR(255),
    `Activo` BOOLEAN
) CHARACTER SET 'UTF8';


CREATE TABLE `18 Compra Insumos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Producto` VARCHAR(255),
    `Cantidad` INTEGER,
    `Valor` DOUBLE
) CHARACTER SET 'UTF8';



CREATE TABLE `23 Ventas` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Lote` VARCHAR(255),
    `Nro Machos` INTEGER,
    `Nro Hembras` INTEGER,
    `Tipo` VARCHAR(255),
    `Peso` INTEGER,
    `Cliente` VARCHAR(255),
    `Planta de sacrificio` VARCHAR(255),
    `Vehiculo que transporta` VARCHAR(255),
    `Cuarentena` VARCHAR(255),
    `Precio Total` DOUBLE,
    `Remisión` VARCHAR(255),
    `Costo flete` DOUBLE,
    `Pago` BOOLEAN
) CHARACTER SET 'UTF8';


CREATE TABLE `24 Clientes` (
    `Id` INTEGER PRIMARY KEY,
    `Nombre cliente` VARCHAR(255),
    `Pesona contacto` VARCHAR(255),
    `Teléfono` DOUBLE,
    `Días de Pago` INTEGER,
    `Activo` BOOLEAN
) CHARACTER SET 'UTF8';


CREATE TABLE `25 Salida Precebo` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Lote` VARCHAR(255),
    `Nro Machos` INTEGER,
    `Nro Hembras` INTEGER,
    `Peso Total` INTEGER,
    `Ubicación` VARCHAR(255),
    `Tipo Salida` VARCHAR(255),
    `Destino` VARCHAR(255),
    `Vehículo` VARCHAR(255),
    `Cuarentena` VARCHAR(255),
    `Precio Total` DOUBLE,
    `Remisión` VARCHAR(255),
    `Valor Flete` DOUBLE
) CHARACTER SET 'UTF8';

CREATE TABLE `26 Traslado de Animales` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Lote de Origen` VARCHAR(255),
    `Lote de Destino` VARCHAR(255),
    `Nro Animales` INTEGER,
    `Causa` VARCHAR(255)
) CHARACTER SET 'UTF8';

CREATE TABLE `27 Traslado Alimento` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Origen` VARCHAR(255),
    `Destino` VARCHAR(255),
    `Referencia Alimento` VARCHAR(255),
    `Cantidad Transferida` INTEGER,
    `Valor Flete` DOUBLE
) CHARACTER SET 'UTF8';


CREATE TABLE `29 Costos Gastos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Descripción` VARCHAR(255),
    `Depreciación/amortización (meses)` INTEGER,
    `Costo` DOUBLE,
    `Granja` VARCHAR(255),
    `Galpón` VARCHAR(255),
    `Lote` VARCHAR(255),
    `Observaciones` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `30 Tipos de Gastos costos` (
    `Id` INTEGER PRIMARY KEY,
    `Descripción` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `31 Consumo Farmacos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Producto` VARCHAR(255),
    `Cantidad` INTEGER,
    `Lote` VARCHAR(255),
    `Ubicacion` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `32 Consumo Alimento` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Referencia Alimento` VARCHAR(255),
    `Cantidad Consumida` INTEGER,
    `Lote` VARCHAR(255),
    `Ubicación` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `33 Consumo Insumos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Granja` VARCHAR(255),
    `Producto` VARCHAR(255),
    `Cantidad` INTEGER,
    `Lote` VARCHAR(255),
    `Ubicacion` VARCHAR(255)
) CHARACTER SET 'UTF8';

CREATE TABLE `34 Tratamientos` (
    `Id` INTEGER PRIMARY KEY,
    `Fecha` DATETIME,
    `Causa` VARCHAR(255),
    `Lote` VARCHAR(255),
    `Cantidad` INTEGER,
    `Galpon` VARCHAR(255),
    `Corral` VARCHAR(255),
    `Edad` INTEGER,
    `Medicamento` VARCHAR(255),
    `Laboratorio` VARCHAR(255),
    `Lote de medicamento` VARCHAR(255),
    `ICA` VARCHAR(255),
    `Dosis` DATETIME,
    `Duración` INTEGER,
    `Retiro` DATETIME,
    `Via de aplicación` VARCHAR(255),
    `Observaciones` VARCHAR(255),
    `Responsable` VARCHAR(255)
) CHARACTER SET 'UTF8';

CREATE TABLE `35 Curvas Crecimiento` (
    `Id` INTEGER PRIMARY KEY,
    `Curva Crecimiento` VARCHAR(255),
    `Edad` INTEGER,
    `Peso` DOUBLE,
    `Consumo` DOUBLE
) CHARACTER SET 'UTF8';


CREATE TABLE `03 Metas PC` (
    `Id` INTEGER PRIMARY KEY,
    `Granja` INTEGER,
    `Etapa` VARCHAR(255),
    `Peso Inicial` DOUBLE,
    `Edad Inicial` INTEGER,
    `Peso Final` DOUBLE,
    `Mortalidad` DOUBLE,
    `Conversión` DOUBLE,
    `Ganancia Peso` DOUBLE,
    `GDP` DOUBLE,
    `Densidad` DOUBLE,
    `Días de permanencia` DOUBLE,
    `Consumo Total` DOUBLE,
    `Consumo/Animal/Día` DOUBLE
) CHARACTER SET 'UTF8';

CREATE TABLE `03 Metas PC_Granja` (
    `_Granja` INTEGER,
    `3 Metas PC_Granja` INTEGER PRIMARY KEY,
    `Value` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `04 Metas Ceba` (
    `Id` INTEGER PRIMARY KEY,
    `Granja` INTEGER,
    `Peso Inicial` DOUBLE,
    `Edad Inicial` INTEGER,
    `Peso Final` DOUBLE,
    `Mortalidad` DOUBLE,
    `Descarte` DOUBLE,
    `Conversión` DOUBLE,
    `Ganancia Peso` DOUBLE,
    `GDP` DOUBLE,
    `Densidad` DOUBLE,
    `Días de permanencia` DOUBLE,
    `Consumo Total` DOUBLE,
    `Consumo/Animal/Día` DOUBLE,
    `Costo Producción` DOUBLE
) CHARACTER SET 'UTF8';



CREATE TABLE `04 Metas Ceba_Granja` (
    `_Granja` INTEGER,
    `4 Metas Ceba_Granja` INTEGER PRIMARY KEY,
    `Value` VARCHAR(255)
) CHARACTER SET 'UTF8';


CREATE TABLE `05 Metas Destete Finalización` (
    `Id` INTEGER PRIMARY KEY,
    `Granja` INTEGER,
    `Peso Inicial` DOUBLE,
    `Edad Inicial` INTEGER,
    `Peso Final` DOUBLE,
    `Mortalidad` DOUBLE,
    `Descarte` DOUBLE,
    `Conversión` DOUBLE,
    `Ganancia Peso` DOUBLE,
    `GDP` DOUBLE,
    `Densidad` DOUBLE,
    `Días de permanencia` DOUBLE,
    `Consumo Total` DOUBLE,
    `Consumo/Animal/Día` DOUBLE,
    `Costo Producción` DOUBLE
) CHARACTER SET 'UTF8';


CREATE TABLE `05 Metas Destete Finalización_Granja` (
    `_Granja` INTEGER,
    `Metas Destete Finalización_Granja` INTEGER PRIMARY KEY,
    `Value` VARCHAR(255)
) CHARACTER SET 'UTF8';
'''