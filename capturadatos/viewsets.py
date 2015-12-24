# -*- encoding: utf-8 -*-
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import filters

class Patologias_grupoViewSet(viewsets.ModelViewSet):
    serializer_class = Patologias_grupoSerializer
    queryset = Patologias_grupo.objects.all()
    permission_classes = [permissions.AllowAny,]

class PatologiasViewSet(viewsets.ModelViewSet):
    serializer_class = PatologiasSerializer
    queryset = Patologias.objects.all()
    permission_classes = [permissions.AllowAny,]

class Medicamentos_laboratorioViewSet(viewsets.ModelViewSet):
    serializer_class = Medicamentos_laboratorioSerializer
    queryset = Medicamentos_laboratorio.objects.all()
    permission_classes = [permissions.AllowAny,]

class Medicamentos_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Medicamentos_tipoSerializer
    queryset = Medicamentos_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class Medicamentos_indicacioneViewSet(viewsets.ModelViewSet):
    serializer_class = Medicamentos_indicacioneSerializer
    queryset = Medicamentos_indicacione.objects.all()
    permission_classes = [permissions.AllowAny,]

class MedicamentoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentoSerializer
    queryset = Medicamento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Traslados_animaleViewSet(viewsets.ModelViewSet):
    serializer_class = Traslados_animaleSerializer
    queryset = Traslados_animale.objects.all()
    permission_classes = [permissions.AllowAny,]
    
class Traslados_alimentoViewSet(viewsets.ModelViewSet):
    serializer_class = Traslados_alimentoSerializer
    queryset = Traslados_alimento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Salidas_placeboViewSet(viewsets.ModelViewSet):
    serializer_class = Salidas_placeboSerializer
    queryset = Salidas_placebo.objects.all()
    permission_classes = [permissions.AllowAny,]    

class TratamientosViewSet(viewsets.ModelViewSet):
    serializer_class = TratamientosSerializer
    queryset = Tratamientos.objects.all()
    permission_classes = [permissions.AllowAny,] 

class animales_geneticaViewSet(viewsets.ModelViewSet):
    serializer_class = animales_geneticaSerializer
    queryset = animales_genetica.objects.all()
    permission_classes = [permissions.AllowAny,]

class animaleViewSet(viewsets.ModelViewSet):
    serializer_class = animaleSerializer
    queryset = animale.objects.all()
    permission_classes = [permissions.AllowAny,]

class mortalidadViewSet(viewsets.ModelViewSet):
    serializer_class = mortalidadSerializer
    queryset = mortalidad.objects.all()
    permission_classes = [permissions.AllowAny,]