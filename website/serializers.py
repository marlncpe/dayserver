# -*- encoding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from granjas.serializers import *
 
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username','password')

    def create(self, validated_data):
        user = User(email=validated_data('email'), username=validated_data('username'))
        user.set_password(validated_data('password'))
        user.save()
        return user

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('id','nombre', 'descripcion', 'fecha_registro')

class Alimentos_fabricaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_fabrica
		fields = ('id','nombre','status','fecha_registro',)

class Alimentos_faseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_fase
		fields = ('id','nombre','descripcion','fecha_registro',)

class Alimentos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_tipo
		fields = ('id','nombre','descripcion','fecha_registro',)

class AlimentoSerializer(serializers.HyperlinkedModelSerializer):
	#fabrica = Alimentos_fabricaSerializer()
	#fase = Alimentos_faseSerializer()
	#tipo_alimento = Alimentos_tipoSerializer()
	class Meta:
		model = Alimento
		fields = ('id','fabrica','fase','tipo_alimento','nombre','presentacion','kg_bulto','status','fecha_registro',)


class Mano_obras_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mano_obras_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class Mano_obraSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Mano_obra
		fields = ('id','granja','fecha_inicial','fecha_final','tipo','detalle','num_personas_pagadas','valor_total',)

class personalSerializer(serializers.ModelSerializer):#pendiente con esta tabla me parece q es redundante
	class Meta:
		model = personal
		fields = ('id','nombres','apellidos','siglas','centro_costo','fecha_ingreso','fecha_retiro','status','eps','contacto',)

class InsumoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Insumo
		fields = ('id','descripcion','Marca','presentacion','unidades_paquetes','status','fecha_registro',)

class Pedidos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pedidos_tipo
		fields = ('id','nombre','descripcion','fecha_registro',)

class PedidoSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#tipo = Pedidos_tipoSerializer()
	class Meta:
		model = Pedido
		fields = ('id','granja','tipo','fecha','subtotal','total','fecha_registro',)

class pedidos_medicamentos_extendidoSerializer(serializers.HyperlinkedModelSerializer):
	#pedido = PedidoSerializer() 
	class Meta:
		model = pedidos_medicamentos_extendido
		fields = ('id','pedido','producto','Cantidad','valor',)

class pedidos_alimentos_extendidoSerializer(serializers.HyperlinkedModelSerializer):
	#pedido = PedidoSerializer() 
	class Meta:
		model = pedidos_alimentos_extendido
		fields = ('id','pedido','producto','Cantidad','valor',)

class pedidos_insumos_extendidoSerializer(serializers.HyperlinkedModelSerializer):
	#pedido = PedidoSerializer() 
	class Meta:
		model = pedidos_insumos_extendido
		fields = ('id','pedido','producto','Cantidad','valor',)

class Compras_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compras_tipo
		fields = ('id','nombre','descripcion','fecha_registro',)

class CompraSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#tipo = Compras_tipoSerializer()
	class Meta:
		model = Compra
		fields = ('id','granja','tipo','fecha','subtotal','total','fecha_registro',)

class Compras_insumoSerializer(serializers.HyperlinkedModelSerializer):
	#compra = CompraSerializer()
	class Meta:
		model = Compras_insumo
		fields = ('id','compra','producto','cantidad','valor',)

class Compras_medicamentoSerializer(serializers.HyperlinkedModelSerializer):
	#compra = CompraSerializer()
	class Meta:
		model = Compras_medicamento
		fields = ('id','compra','producto','lote','cantidad','valor',)

class Compras_alimentoSerializer(serializers.HyperlinkedModelSerializer):
	#compra = CompraSerializer()
	class Meta:
		model = Compras_alimento
		fields = ('id','compra','referencia','lote','cantidad','valor','medicado','dosis_medicado','valor_medicado',)

class MedicadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicado
		fields = ('id','producto','Principio','referencia','status','fecha_registro',)


class ventasSerializer(serializers.ModelSerializer):
	class Meta:
		model = ventas
		fields = ('id','lote','num_machos','num_hembras','tipo','peso','cliente','planta_sacrificio','vehiculo','cuarentena','precio_total','remision','costos_flete','pago','fecha_registro',)

class Costos_gastoSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#Galpon = GalponombreSerializer()
	class Meta:
		model = Costos_gasto
		fields = ('id','granja','Galpon','lote','descripcion','amortizacion','costos','observaciones','fecha_registro',)

class Consumos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Consumos_tipo
		fields = ('id','nombre','descripcion','fecha_registro',)

class ConsumoSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#tipo = Consumos_tipoSerializer()
	class Meta:
		model = Consumo
		fields = ('id','granja','lote','tipo','fecha_registro',)

class Consumos_farmacoSerializer(serializers.HyperlinkedModelSerializer):
	#consumo = ConsumoSerializer()
	class Meta:
		model = Consumos_farmaco
		fields = ('id','consumo','producto','cantidad','ubicacion',) 

class Consumos_alimentoSerializer(serializers.HyperlinkedModelSerializer):
	#consumo = ConsumoSerializer()
	class Meta:
		model = Consumos_alimento
		fields = ('id','consumo','referencia','cantidad','ubicacion',) 

class Consumos_insumoSerializer(serializers.HyperlinkedModelSerializer):
	#consumo = ConsumoSerializer()
	class Meta:
		model = Consumos_insumo
		fields = ('id','consumo','producto','cantidad','ubicacion',) 

class Curvas_crecimientoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Curvas_crecimiento
		fields = ('id','curva','edad','peso','consumo','fecha_registro',) 

class Metas_pcSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Metas_pc
		fields = ('id','granja','etapa','peso_inicial','edad_inicial','peso_final','mortalidad','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','fecha_registro',) 

class Metas_cebaSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Metas_ceba
		fields = ('id','granja','peso_inicial','edad_inicial','peso_final','mortalidad','descarte','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','costos_produccion','fecha_registro',) 

class Metas_destete_finalizacioneSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Metas_destete_finalizacione
		fields = ('id','granja','peso_inicial','edad_inicial','peso_final','mortalidad','descarte','conversion','ganacia_peso','gdp','densidad','dias_permanencia','consumo_total','consumo_animal_diario','costos_produccion','fecha_registro',) 

class RecordatorioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recordatorio
		fields = ('id','tipo','fecha_recordatorio','fecha_registro',) 

class Recordatorios_extendidoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Recordatorios_extendido
		fields = ('id','nombre','descripcion','fecha_registro',) 
