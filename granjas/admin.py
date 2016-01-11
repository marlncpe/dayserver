# -*- encoding: utf-8 -*-
from django.contrib import admin
from models import *


# Register your models here.

class Granjas_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class GranjaAdmin(admin.ModelAdmin):
    list_display = ['nombre','tipo_granja','area','ubicacion','fecha_registro',]

class GalponeAdmin(admin.ModelAdmin):
    list_display = ['nombre','numero','fecha_registro',]

class CorraleAdmin(admin.ModelAdmin):
    list_display = ['numero','area_disponible','capacidad','fecha_registro',]

class InmunocastracioneAdmin(admin.ModelAdmin):
    list_display = ['granja','rastro','pdosis','sdosis','tdosis','periodo_venta','fecha_registro',]

#class Inmunocastraciones_extendidaAdmin(admin.ModelAdmin):
#    list_display = ['Inmunocastracion','numero','fecha_aplicacion','fecha_registro',]
class animales_permitidosAdmin(admin.ModelAdmin):
    list_display = ['id','cantidad','granja','dueno','encargado_asignacion','fecha_registro']

admin.site.register(Granjas_tipo, Granjas_tipoAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Galpone, GalponeAdmin)
admin.site.register(Corrale, CorraleAdmin)
admin.site.register(Inmunocastracione, InmunocastracioneAdmin)
admin.site.register(animales_permitidos, animales_permitidosAdmin)

#admin.site.register(Inmunocastraciones_extendida, Inmunocastraciones_extendidaAdmin)
