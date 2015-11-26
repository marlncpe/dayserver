# -*- encoding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
 
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','username','password')
        permission_classes = (IsAdminUser,)

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('nombre', 'descripcion', 'fecha_registro')

class Granjas_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Granjas_tipo
		fields = ('nombre','descripcion','fecha_registro')

#B clase solo para extraer nombre del tipo de granja
class Granjas_tiponameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Granjas_tipo
		fields = ('nombre',)
#End

class GranjaSerializer(serializers.ModelSerializer):
	tipo_granja = Granjas_tiponameSerializer()
	class Meta:
		model = Granja
		fields = ('nombre','tipo_granja','area','ubicacion','fecha_registro',)

#B clase solo para extraer nombre de la granja
class GranjanombreSerializer(serializers.ModelSerializer):
	tipo_granja = Granjas_tiponameSerializer()
	class Meta:
		model = Granja
		fields = ('nombre','tipo_granja',)
#End
	
class GalponeSerializer(serializers.ModelSerializer):
    granja = GranjanombreSerializer()
    class Meta:
		model = Galpone
		fields = ('granja','nombre','numero','fecha_registro',)

#B clase solo para extraer nombre del galpon
class GalponombreSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	class Meta:
		model = Galpone
		fields = ('granja','nombre',)
#End

class CorraleSerializer(serializers.ModelSerializer):
	galpon = GalponombreSerializer()
	class Meta:
		model = Corrale
		fields = ('galpon','numero','area_disponible','capacidad','fecha_registro',)

class InmunocastracioneSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	class Meta:
		model = Inmunocastracione
		fields = ['granja','rastro','periodo_venta','fecha_registro',]

class Inmunocastraciones_extendidaSerializer(serializers.ModelSerializer):
	Inmunocastracion = InmunocastracioneSerializer()
	class Meta:
		model = Inmunocastraciones_extendida
		fields = ('Inmunocastracion','numero','fecha_aplicacion','fecha_registro',)

class Alimentos_fabricaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_fabrica
		fields = ('nombre','status','fecha_registro',)

class Alimentos_faseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_fase
		fields = ('nombre','descripcion','fecha_registro',)

class Alimentos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alimentos_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class AlimentoSerializer(serializers.ModelSerializer):
	fabrica = Alimentos_fabricaSerializer()
	fase = Alimentos_faseSerializer()
	tipo_alimento = Alimentos_tipoSerializer()
	class Meta:
		model = Alimento
		fields = ('fabrica','fase','tipo_alimento','nombre','presentacion','kg_bulto','status','fecha_registro',)

class Patologias_grupoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patologias_grupo
		fields = ('nombre','descripcion','fecha_registro',)

class PatologiasSerializer(serializers.ModelSerializer):
	grupo = Patologias_grupoSerializer()
	class Meta:
		model = Patologias
		fields = ('casusa','grupo','causa_muerte','causa_descarte','causa_tratamiento','status','fecha_registro',)

class Medicamentos_laboratorioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicamentos_laboratorio
		fields = ('nombre','descripcion','registro_comercial','fecha_registro',)

class Medicamentos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicamentos_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class MedicamentoSerializer(serializers.ModelSerializer):
	laboratorio = Medicamentos_laboratorioSerializer()
	tipo = Medicamentos_tipoSerializer()
	class Meta:
		model = Medicamento
		fields = ('nombre','Laboratorio','registro_ica','presentacion','tipo','status','fecha_registro',)

class Medicamentos_indicacioneSerializer(serializers.ModelSerializer):
	medicamento = MedicamentoSerializer()
	class Meta:
		model = Medicamentos_indicacione
		fields = ('medicamento','indicacion','descripcion','fecha_registro',)

class Mano_obras_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mano_obras_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class Mano_obraSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	class Meta:
		model = Mano_obra
		fields = ('granja','fecha_inicial','fecha_final','tipo','detalle','num_personas_pagadas','valor_total',)

class personalSerializer(serializers.ModelSerializer):#pendiente con esta tabla me parece q es redundante
	class Meta:
		model = personal
		fields = ('nombres','apellidos','siglas','centro_costo','fecha_ingreso','fecha_retiro','status','eps','contacto',)

class InsumoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Insumo
		fields = ('descripcion','Marca','presentacion','unidades_paquetes','status','fecha_registro',)

class Pedidos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Pedidos_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class PedidoSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	tipo = Pedidos_tipoSerializer()
	class Meta:
		model = Pedido
		fields = ('granja','tipo','fecha','subtotal','total','fecha_registro',)

class pedidos_medicamentos_extendidoSerializer(serializers.ModelSerializer):
	pedido = PedidoSerializer() 
	class Meta:
		model = pedidos_medicamentos_extendido
		fields = ('pedido','producto','Cantidad','valor',)

class pedidos_alimentos_extendidoSerializer(serializers.ModelSerializer):
	pedido = PedidoSerializer() 
	class Meta:
		model = pedidos_alimentos_extendido
		fields = ('pedido','referencia','medicado','dosis','fecha_recogida','observaciones','valor',)

class animales_geneticaSerializer(serializers.ModelSerializer):
	class Meta:
		model = animales_genetica
		fields = ('nombre','descripcion','fecha_registro',)

class animaleSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	galpon = GalponombreSerializer()
	corral = CorraleSerializer()
	genetica = animales_geneticaSerializer()
	class Meta:
		model = animale
		fields = ('granja','galpon','corrales','lote','edad','num_machos','num_hembras','peso_total','remision','valor_lote','procedencia','genetica','observaciones','status',)

class mortalidadSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	galpon = GalponombreSerializer()
	corral = CorraleSerializer()
	class Meta:
		model = mortalidad
		fields = ('granja','galpon','corral','fecha','lote','sexo','causa','cantidad','peso','destino',)

class Compras_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compras_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class CompraSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	tipo = Compras_tipoSerializer()
	class Meta:
		model = Compra
		fields = ('granja','tipo','fecha','subtotal','total','fecha_registro',)

class Compras_insumoSerializer(serializers.ModelSerializer):
	compra = CompraSerializer()
	class Meta:
		model = Compras_insumo
		fields = ('compra','producto','cantidad','valor',)

class Compras_medicamentoSerializer(serializers.ModelSerializer):
	compra = CompraSerializer()
	class Meta:
		model = Compras_medicamento
		fields = ('compra','producto','lote','cantidad','valor',)

class Compras_alimentoSerializer(serializers.ModelSerializer):
	compra = CompraSerializer()
	class Meta:
		model = Compras_alimento
		fields = ('compra','referencia','lote','cantidad','valor','medicado','dosis_medicado','valor_medicado',)