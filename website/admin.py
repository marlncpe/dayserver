# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.


# Register your models here.

class StatusAdmin(admin.ModelAdmin):
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
    list_display = ['granja','rastro','periodo_venta','fecha_registro',]

class Inmunocastraciones_extendidaAdmin(admin.ModelAdmin):
    list_display = ['Inmunocastracion','numero','fecha_aplicacion','fecha_registro',]

class Alimentos_fabricaAdmin(admin.ModelAdmin):
    list_display = ['nombre','status','fecha_registro',]

class Alimentos_faseAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class Alimentos_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['fabrica','fase','nombre','presentacion','kg_bulto','tipo_alimento','status','fecha_registro',]

class patologias_grupoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class patologiasAdmin(admin.ModelAdmin):
    list_display = ['casusa','grupo','causa_muerte','causa_descarte','causa_tratamiento','status','fecha_registro',]

class Medicamentos_laboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','registro_comercial','fecha_registro',]

class Medicamentos_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre','Laboratorio','registro_ica','presentacion','tipo','status','fecha_registro',]

class Medicamentos_indicacioneAdmin(admin.ModelAdmin):
    list_display = ['medicamento','indicacion','descripcion','fecha_registro',]

class Mano_obras_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class Mano_obraAdmin(admin.ModelAdmin):
    list_display = ['granja','fecha_inicial','fecha_final','tipo','detalle','num_personas_pagadas','valor_total',]

class personalAdmin(admin.ModelAdmin):#pendiente con esta tabla me parece q es redundante
    list_display = ['nombres','apellidos','siglas','centro_costo','fecha_ingreso','fecha_retiro','status','eps','contacto',]

class InsumoAdmin(admin.ModelAdmin):
    list_display = ['descripcion','Marca','presentacion','unidades_paquetes','status','fecha_registro',]

class Pedidos_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['granja','tipo','fecha','subtotal','total','fecha_registro',]

class pedidos_medicamentos_extendidoAdmin(admin.ModelAdmin):
    list_display = ['pedido','producto','Cantidad','valor',]

class pedidos_alimentos_extendidoAdmin(admin.ModelAdmin):
    list_display = ['pedido','referencia','medicado','dosis','fecha_recogida','observaciones','valor',]

class animales_geneticaAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class animaleAdmin(admin.ModelAdmin):
    list_display = ['granja','galpon','corrales','lote','edad','num_machos','num_hembras','peso_total','remision','valor_lote','procedencia','genetica','observaciones','status',]

class mortalidadAdmin(admin.ModelAdmin):
    list_display = ['granja','galpon','corral','fecha','lote','sexo','causa','cantidad','peso','destino',]

class Compras_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class CompraAdmin(admin.ModelAdmin):
    list_display = ['granja','tipo','fecha','subtotal','total','fecha_registro',]

class Compras_insumoAdmin(admin.ModelAdmin):
    list_display = ['compra','producto','cantidad','valor',]

class Compras_medicamentoAdmin(admin.ModelAdmin):
    list_display = ['compra','producto','lote','cantidad','valor',]

class Compras_alimentoAdmin(admin.ModelAdmin):
    list_display = ['compra','referencia','lote','cantidad','valor','medicado','dosis_medicado','valor_medicado',]

class MedicadoAdmin(admin.ModelAdmin):
    list_display = ['producto','Principio','referencia','status','fecha_registro',]

class Traslados_animaleAdmin(admin.ModelAdmin):
    list_display = ['granja','lote_origen','lote_destino','nro_animales','causa',]

class Traslados_alimentoAdmin(admin.ModelAdmin):
    list_display = ['granja','origen','destino','referencia','cantidad','valor_flete',]

class ventasAdmin(admin.ModelAdmin):
    list_display = ['lote','num_machos','num_hembras','tipo','peso','cliente','planta_sacrificio','vehiculo','cuarentena','precio_total','remision','costos_flete','pago','fecha_registro',]

class Costos_gastoAdmin(admin.ModelAdmin):
    list_display = ['granja','Galpon','lote','descripcion','amortizacion','costos','observaciones','fecha_registro',] 

class Consumos_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',] 

class ConsumoAdmin(admin.ModelAdmin):
    list_display = ['granja','lote','fecha_registro',] 

class Consumos_farmacoAdmin(admin.ModelAdmin):
    list_display = ['consumo','producto','cantidad','ubicacion',] 

class Consumos_alimentoAdmin(admin.ModelAdmin):
    list_display = ['consumo','referencia','cantidad','ubicacion',] 

class Consumos_insumoAdmin(admin.ModelAdmin):
    list_display = ['consumo','producto','cantidad','ubicacion',] 

class Salidas_placeboAdmin(admin.ModelAdmin):
    list_display = ['lote','num_machos','num_hembras','peso_total','ubicacion','tipo_salida','destino','vehiculo','cuarentena','precio_total','remision','valor_flete','fecha_registro',] 

class TratamientosAdmin(admin.ModelAdmin):
    list_display = ['granja','Galpon','corral','causa','lote','cantidad','edad','medicamento','laboratorio','lote_medicamento','ICA','dosis','duracion','retiro','via_aplicacion','observaciones','responsable','fecha_registro',] 

class Curvas_crecimientoAdmin(admin.ModelAdmin):
    list_display = ['curva','edad','peso','consumo','fecha_registro',] 

class Metas_pcAdmin(admin.ModelAdmin):
    list_display = ['granja','etapa','peso_inicial','edad_inicial','peso_final','mortalidad','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','fecha_registro',] 

class Metas_cebaAdmin(admin.ModelAdmin):
    list_display = ['granja','peso_inicial','edad_inicial','peso_final','mortalidad','descarte','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','costos_produccion','fecha_registro',] 

class Metas_destete_finalizacioneAdmin(admin.ModelAdmin):
    list_display = ['granja','peso_inicial','edad_inicial','peso_final','mortalidad','descarte','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','costos_produccion','fecha_registro',] 



admin.site.register(Status, StatusAdmin)
admin.site.register(Usuarios_permiso, Usuarios_permisoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
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