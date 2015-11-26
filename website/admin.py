# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.


# Register your models here.

class statusAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','fecha_registro',]

class Usuarios_permisoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_registro',]

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','nacionalidad','cedula','direccion','telefono','foto','tipo_permiso','respuesta_seguridad','persona_contacto','dias_pago','status',]

class Granjas_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class GranjaAdmin(admin.ModelAdmin):
    list_display = ['nombre','tipo_granja','area','ubicacion','fecha_registro',]

class GalponeAdmin(admin.ModelAdmin):
    list_display = ['granja','nombre','numero','fecha_registro',]

class CorraleAdmin(admin.ModelAdmin):
    list_display = ['galpon','numero','area_disponible','capacidad','fecha_registro',]

class InmunocastracioneAdmin(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    rastro = models.CharField(max_length=11,blank=True)
    periodo_venta = models.CharField(max_length=11,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Inmunocastraciones_extendida(admin.ModelAdmin):
    Inmunocastracion = models.ForeignKey(Inmunocastracione)
    numero = models.CharField(max_length=50,blank=False)
    fecha_aplicacion = models.CharField(max_length=10,blank=True) 
    fecha_registro = models.DateField(auto_now_add=True)

class Alimentos_fabrica(admin.ModelAdmin):
    nombre = models.CharField(max_length=255,blank=False)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimentos_fase(admin.ModelAdmin):
    nombre = models.CharField(max_length=50,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimentos_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class Alimento(admin.ModelAdmin):
    fabrica = models.ForeignKey(Alimentos_fabrica)
    fase = models.ForeignKey(Alimentos_fase)
    nombre = models.CharField(max_length=255, blank=False)
    presentacion = models.CharField(max_length=255,blank=True)
    kg_bulto = models.CharField(max_length=11,blank=False)
    tipo_alimento = models.ForeignKey(Alimentos_tipo)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class patologias_grupo(admin.ModelAdmin):
    nombre = models.CharField(max_length=255,blank=False)
    descripcion = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

class patologias(admin.ModelAdmin):
    casusa = models.CharField(max_length=255,blank=False)
    grupo = models.ForeignKey(patologias_grupo)
    causa_muerte = models.CharField(max_length=50, blank=True)
    causa_descarte = models.CharField(max_length=50, blank=True) 
    causa_tratamiento = models.CharField(max_length=50, blank=True)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_laboratorio(admin.ModelAdmin):
    nombre = models.CharField(max_length=255,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    registro_comercial = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=100,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamento(admin.ModelAdmin):
    nombre = models.CharField(max_length=255,blank=False)
    Laboratorio = models.ForeignKey(Medicamentos_laboratorio)
    registro_ica = models.CharField(max_length=255, blank=False)
    presentacion = models.CharField(max_length=255, blank=True)
    tipo = models.ForeignKey(Medicamentos_tipo)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Medicamentos_indicacione(admin.ModelAdmin):
    medicamento = models.ForeignKey(Medicamento)
    indicacion = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=False)
    fecha_registro = models.DateField(auto_now_add=True)

class Mano_obras_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Mano_obra(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    fecha_inicial = models.DateField(auto_now_add=False)
    fecha_final = models.DateField(auto_now_add=False)
    tipo = models.ForeignKey(Mano_obras_tipo)
    detalle = models.CharField(max_length=255,blank=True)
    num_personas_pagadas = models.CharField(max_length=11, blank=False)
    valor_total = models.CharField(max_length=11 ,blank=False)

class personal(admin.ModelAdmin):#pendiente con esta tabla me parece q es redundante
    nombres = models.CharField(max_length=60, blank=False)
    apellidos = models.CharField(max_length=60, blank=False)
    siglas = models.CharField(max_length=4, blank=True)
    centro_costo = models.CharField(max_length=255, blank=True)
    fecha_ingreso = models.CharField(max_length=10, blank=False)
    fecha_retiro = models.CharField(max_length=10, blank=True)
    status = models.ForeignKey(status)
    eps = models.CharField(max_length=255, blank=True)
    contacto = models.CharField(max_length=16, blank=True)

class Insumo(admin.ModelAdmin):
    descripcion = models.CharField(max_length=255, blank=False)
    Marca = models.CharField(max_length=50, blank=True)
    presentacion = models.CharField(max_length=50, blank=True)
    unidades_paquetes = models.CharField(max_length=11, blank=False)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Pedidos_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=10,blank=False)
    descripcion = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Pedido(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    tipo = models.ForeignKey(Pedidos_tipo)
    fecha = models.CharField(max_length=10, blank=False)
    subtotal = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class pedidos_medicamentos_extendido(admin.ModelAdmin):
    pedido = models.ForeignKey(Pedido)
    producto = models.CharField(max_length=255,blank=False)
    Cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class pedidos_alimentos_extendido(admin.ModelAdmin):
    pedido = models.ForeignKey(Pedido)
    referencia = models.CharField(max_length=255,blank=True)
    medicado = models.CharField(max_length=255, blank=True)
    dosis = models.CharField(max_length=15, blank=True)
    fecha_recogida = models.CharField(max_length=10, blank=False)
    observaciones = models.CharField(max_length=255, blank=True)
    valor = models.CharField(max_length=12, blank=False)

class animales_genetica(admin.ModelAdmin):
    nombre = models.CharField(max_length=100,blank=False)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class animale(admin.ModelAdmin):
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

class mortalidad(admin.ModelAdmin):
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


class Compras_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=10,blank=False)
    descripcion = models.CharField(max_length=255,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Compra(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    tipo = models.ForeignKey(Pedidos_tipo)
    fecha = models.CharField(max_length=10, blank=False)
    subtotal = models.CharField(max_length=10, blank=True)
    total = models.CharField(max_length=10,blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Compras_insumo(admin.ModelAdmin):
    compra = models.ForeignKey(Compra)
    producto = models.CharField(max_length=255,blank=False)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class Compras_medicamento(admin.ModelAdmin):
    compra = models.ForeignKey(Compra)
    producto = models.CharField(max_length=255,blank=False)
    lote = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)

class Compras_alimento(admin.ModelAdmin):
    compra = models.ForeignKey(Compra)
    referencia = models.CharField(max_length=255,blank=True)
    lote = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=12, blank=False)
    valor = models.CharField(max_length=12, blank=False)
    medicado = models.CharField(max_length=255,blank=True)
    dosis_medicado = models.CharField(max_length=12, blank=True)
    valor_medicado = models.CharField(max_length=12, blank=True)

class Medicado(admin.ModelAdmin):
    producto = models.CharField(max_length=255, blank=True)
    Principio = models.CharField(max_length=255, blank=True)
    referencia = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Traslados_animale(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    lote_origen = models.CharField(max_length=255, blank=True)
    lote_destino = models.CharField(max_length=255, blank=True)
    nro_animales = models.CharField(max_length=255, blank=True)
    causa = models.CharField(max_length=255, blank=True)

class Traslados_alimento(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    origen = models.CharField(max_length=255, blank=True)
    destino = models.CharField(max_length=255, blank=True)
    referencia = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=16, blank=True)
    valor_flete = models.CharField(max_length=16, blank=True)

class ventas(admin.ModelAdmin):
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
    pago = models.ForeignKey(status)
    fecha_registro = models.DateField(auto_now_add=True)

class Costos_gasto(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    Galpon = models.ForeignKey(Galpone)
    lote = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    amortizacion = models.CharField(max_length=255, blank=True)
    costos = models.CharField(max_length=255, blank=True)
    observaciones = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumos_tipo(admin.ModelAdmin):
    nombre = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumo(admin.ModelAdmin):
    granja = models.ForeignKey(Granja)
    lote = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Consumos_farmaco(admin.ModelAdmin):
    consumo = models.ForeignKey(Consumo)
    producto = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Consumos_alimento(admin.ModelAdmin):
    consumo = models.ForeignKey(Consumo)
    referencia = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Consumos_insumo(admin.ModelAdmin):
    consumo = models.ForeignKey(Consumo)
    producto = models.CharField(max_length=255, blank=True)
    cantidad = models.CharField(max_length=255, blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)

class Salidas_placebo(admin.ModelAdmin):
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

class Tratamientos(admin.ModelAdmin):
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

class Curvas_crecimiento(admin.ModelAdmin):
    curva = models.CharField(max_length=255, blank=True)
    edad = models.CharField(max_length=255, blank=True)
    peso = models.CharField(max_length=255, blank=True)
    consumo = models.CharField(max_length=255, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)

class Metas_pc(admin.ModelAdmin):
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

class Metas_ceba(admin.ModelAdmin):
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

class Metas_destete_finalizacione(admin.ModelAdmin):
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



admin.site.register(status, statusAdmin)
admin.site.register(Usuarios_permiso, Usuarios_permisoAdmin)
admin.site.register(UserProfileAdmin, UserProfile)
admin.site.register(Granjas_tipo, Granjas_tipoAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Galpone, GalponeAdmin)
admin.site.register(Inmunocastracione, InmunocastracioneAdmin)
admin.site.register(Inmunocastraciones_extendida, Inmunocastraciones_extendidaAdmin)
admin.site.register(Alimentos_fabrica, Alimentos_fabricaAdmin)
admin.site.register(Alimentos_fase,Alimentos_faseAdmin)
admin.site.register(Alimentos_tipo,Alimentos_tipoAdmin)
admin.site.register(Alimento,AlimentoAdmin)
admin.site.register(patologias_grupo,patologias_grupoAdmin)
admin.site.register(patologias,patologiasAdmin)
admin.site.register(Medicamentos_laboratorio,Medicamentos_laboratorioAdmin)
admin.site.register(Medicamentos_tipo,Medicamentos_tipoAdmin)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Medicamentos_indicacione,Medicamentos_indicacioneAdmin)
admin.site.register(Mano_obras_tipo,Mano_obras_tipoAdmin)
admin.site.register(Mano_obra,Mano_obraAdmin)
admin.site.register(personal,personalAdmin)
admin.site.register(Insumo,InsumoAdmin)
admin.site.register(Pedidos_tipo,Pedidos_tipoAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(pedidos_medicamentos_extendido,pedidos_medicamentos_extendidoAdmin)
admin.site.register(pedidos_alimentos_extendido,pedidos_alimentos_extendidoAdmin)
admin.site.register(animales_genetica,animales_geneticaAdmin)
admin.site.register(animale,animaleAdmin)
admin.site.register(mortalidad,mortalidadAdmin)
admin.site.register(Compras_tipo,Compras_tipoAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Compras_insumo,Compras_insumoAdmin)
admin.site.register(Compras_medicamento,Compras_medicamentoAdmin)
admin.site.register(Compras_alimento,Compras_alimentoAdmin)
admin.site.register(Medicado,MedicadoAdmin)
admin.site.register(Traslados_animale,Traslados_animaleAdmin)
admin.site.register(Traslados_alimento,Traslados_alimentoAdmin)
admin.site.register(ventas,ventasAdmin)
admin.site.register(Costos_gasto,Costos_gastoAdmin)
admin.site.register(Consumos_tipo,Consumos_tipoAdmin)
admin.site.register(Consumo,ConsumoAdmin)
admin.site.register(Consumos_farmaco,Consumos_farmacoAdmin)
admin.site.register(Consumos_alimento,Consumos_alimentoAdmin)
admin.site.register(Consumos_insumo,Consumos_insumoAdmin)
admin.site.register(Salidas_placebo,Salidas_placeboAdmin)
admin.site.register(Tratamientos,TratamientosAdmin)
admin.site.register(Curvas_crecimiento,Curvas_crecimientoAdmin)
admin.site.register(Metas_pc,Metas_pcAdmin)
admin.site.register(Metas_ceba,Metas_cebaAdmin)
admin.site.register(Metas_destete_finalizacione,Metas_destete_finalizacioneAdmin)