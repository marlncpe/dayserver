# -*- encoding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from granjas.serializers import *

class Patologias_grupoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patologias_grupo
		fields = ('nombre','descripcion','fecha_registro',)

class PatologiasSerializer(serializers.HyperlinkedModelSerializer):
	#grupo = Patologias_grupoSerializer()
	class Meta:
		model = Patologias
		fields = ('id','casusa','grupo','causa_muerte','causa_descarte','causa_tratamiento','status','fecha_registro',)

class animales_geneticaSerializer(serializers.ModelSerializer):
	class Meta:
		model = animales_genetica
		fields = ('nombre','descripcion','fecha_registro',)

class animaleSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#galpon = GalponombreSerializer()
	#corrales = CorraleSerializer()
	#genetica = animales_geneticaSerializer()
	class Meta:
		model = animale
		fields = ('id','granja','galpon','corrales','lote','edad','num_machos','num_hembras','peso_total','remision','valor_lote','procedencia','genetica','observaciones','status',)

class mortalidadSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#galpon = GalponombreSerializer()
	#corral = CorraleSerializer()
	class Meta:
		model = mortalidad
		fields = ('id','granja','galpon','corral','fecha','lote','sexo','causa','cantidad','peso','destino',)


class Medicamentos_laboratorioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicamentos_laboratorio
		fields = ('nombre','descripcion','registro_comercial','fecha_registro',)

class Medicamentos_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Medicamentos_tipo
		fields = ('nombre','descripcion','fecha_registro',)

class MedicamentoSerializer(serializers.HyperlinkedModelSerializer):
	#laboratorio = Medicamentos_laboratorioSerializer()
	#tipo = Medicamentos_tipoSerializer()
	class Meta:
		model = Medicamento
		fields = ('id','nombre','laboratorio','registro_ica','presentacion','tipo','status','fecha_registro',)

class Medicamentos_indicacioneSerializer(serializers.HyperlinkedModelSerializer):
	#medicamento = MedicamentoSerializer()
	class Meta:
		model = Medicamentos_indicacione
		fields = ('medicamento','indicacion','descripcion','fecha_registro',)

class Traslados_animaleSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Traslados_animale
		fields = ('granja','lote_origen','lote_destino','nro_animales','causa','fecha','fecha_registro',)

class Traslados_alimentoSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	class Meta:
		model = Traslados_alimento
		fields = ('granja','origen','destino','referencia','cantidad','valor_flete','fecha','fecha_registro',)

class Salidas_placeboSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Salidas_placebo
		fields = ('granja','galpon','corral','lote','num_machos','num_hembras','peso_total','ubicacion','tipo_salida','destino','vehiculo','cuarentena','precio_total','remision','valor_flete','fecha_registro',)

class TratamientosSerializer(serializers.HyperlinkedModelSerializer):
	#granja = GranjanombreSerializer()
	#galpon = GalponombreSerializer()
	#corral = CorraleSerializer()
	class Meta:
		model = Tratamientos
		fields = ('granja','galpon','corral','causa','lote','cantidad','edad','medicamento','laboratorio','lote_medicamento','ica','dosis','duracion','retiro','via_aplicacion','observaciones','responsable','fecha_registro',) 

