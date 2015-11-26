# -*- encoding: utf-8 -*-
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import filters
from .filters import *

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny,]

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [permissions.AllowAny,]

class Granjas_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Granjas_tipoSerializer
    queryset = Granjas_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class GranjaViewSet(viewsets.ModelViewSet):
    serializer_class = GranjaSerializer
    queryset = Granja.objects.all()
    permission_classes = [permissions.AllowAny,]

class GalponeViewSet(viewsets.ModelViewSet):
    serializer_class = GalponeSerializer
    queryset = Galpone.objects.all()
    permission_classes = [permissions.AllowAny,]

class CorraleViewSet(viewsets.ModelViewSet):
    serializer_class = CorraleSerializer
    queryset = Corrale.objects.all()
    permission_classes = [permissions.AllowAny,]

class InmunocastracioneViewSet(viewsets.ModelViewSet):
    serializer_class = InmunocastracioneSerializer
    queryset = Inmunocastracione.objects.all()
    permission_classes = [permissions.AllowAny,]

class Inmunocastraciones_extendidaViewSet(viewsets.ModelViewSet):
    serializer_class = Inmunocastraciones_extendidaSerializer
    queryset = Inmunocastraciones_extendida.objects.all()
    permission_classes = [permissions.AllowAny,]