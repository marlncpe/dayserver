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
