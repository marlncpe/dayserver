# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.


# Register your models here.

class statusAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','fecha_registro',]

class Usuarios_permisoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_registro',]

class Granjas_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class GranjaAdmin(admin.ModelAdmin):
    list_display = ['nombre','tipo_granja','area','ubicacion','fecha_registro',]

class GalponeAdmin(admin.ModelAdmin):
    list_display = ['granja','nombre','numero','fecha_registro',]

class CorraleAdmin(admin.ModelAdmin):
    list_display = ['galpon','numero','area_disponible','capacidad','fecha_registro',]


admin.site.register(status, statusAdmin)
admin.site.register(Usuarios_permiso, Usuarios_permisoAdmin)
admin.site.register(Granjas_tipo, Granjas_tipoAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Galpone, GalponeAdmin)