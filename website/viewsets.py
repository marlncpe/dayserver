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