# -*- encoding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser


class Granjas_tipoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Granjas_tipo
		fields = ('id','nombre','descripcion','fecha_registro')

#B clase solo para extraer nombre del tipo de granja
class Granjas_tiponameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Granjas_tipo
		fields = ('id','nombre',)
#End

class GranjaSerializer(serializers.HyperlinkedModelSerializer):
	#tipo_granja = Granjas_tiponameSerializer()#serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Granja
		fields = ('id','nombre','tipo_granja','area','ubicacion','dueno','fecha_registro',)

#B clase solo para extraer nombre de la granja
class GranjanombreSerializer(serializers.HyperlinkedModelSerializer):
	tipo_granja = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Granja
		fields = ('id','nombre','dueno',)#'tipo_granja',)
#End
	
class GalponeSerializer(serializers.ModelSerializer):
   # granja = GranjaSerializer()
    class Meta:
		model = Galpone
		fields = ('id','nombre','numero','fecha_registro',)#falta granja
	
    #def create(self, validated_data):
     #   id = validated_data.pop('granja')
     #   granja = Granja.objects.create(**id)
     #   validated_data['granja'] = granja
     #  	galpone = Galpone.objects.create(**validated_data)

#B clase solo para extraer nombre del galpon
class GalponombreSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	class Meta:
		model = Galpone
		fields = ('granja','nombre',)
#End

class CorraleSerializer(serializers.ModelSerializer):
	#galpon = GalponombreSerializer()
	class Meta:
		model = Corrale
		fields = ('id','numero','area_disponible','capacidad','fecha_registro',)#falta galpon

class InmunocastracioneSerializer(serializers.ModelSerializer):
	granja = GranjanombreSerializer()
	class Meta:
		model = Inmunocastracione
		fields = ('id','granja','rastro','periodo_venta','fecha_registro',)

class Inmunocastraciones_extendidaSerializer(serializers.ModelSerializer):
	Inmunocastracion = InmunocastracioneSerializer()
	class Meta:
		model = Inmunocastraciones_extendida
		fields = ('id','Inmunocastracion','numero','fecha_aplicacion','fecha_registro',)