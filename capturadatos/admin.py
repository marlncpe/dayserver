from django.contrib import admin
from granjas.admin import *
from website.admin import *
from models import *
# Register your models here.

class Salidas_placeboAdmin(admin.ModelAdmin):
    list_display = ['lote','num_machos','num_hembras','peso_total','ubicacion','tipo_salida','destino','vehiculo','cuarentena','precio_total','remision','valor_flete','fecha_registro',] 

class TratamientosAdmin(admin.ModelAdmin):
    list_display = ['granja','galpon','corral','causa','lote','cantidad','edad','medicamento','laboratorio','lote_medicamento','ica','dosis','duracion','retiro','via_aplicacion','observaciones','responsable','fecha_registro',] 

class Patologias_grupoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class PatologiasAdmin(admin.ModelAdmin):
    list_display = ['casusa','grupo','causa_muerte','causa_descarte','causa_tratamiento','status','fecha_registro',]

class Medicamentos_laboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','registro_comercial','fecha_registro',]

class Medicamentos_tipoAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre','laboratorio','registro_ica','presentacion','tipo','status','fecha_registro',]

class Medicamentos_indicacioneAdmin(admin.ModelAdmin):
    list_display = ['medicamento','indicacion','descripcion','fecha_registro',]

class animales_geneticaAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','fecha_registro',]

class animaleAdmin(admin.ModelAdmin):
    list_display = ['granja','galpon','corrales','lote','edad','num_machos','num_hembras','peso_total','remision','valor_lote','procedencia','genetica','observaciones','status',]

class mortalidadAdmin(admin.ModelAdmin):
    list_display = ['granja','galpon','corral','fecha','lote','sexo','causa','cantidad','peso','destino',]

class Traslados_animaleAdmin(admin.ModelAdmin):
    list_display = ['granja','lote_origen','lote_destino','nro_animales','causa',]

class Traslados_alimentoAdmin(admin.ModelAdmin):
    list_display = ['granja','origen','destino','referencia','cantidad','valor_flete',]


admin.site.register(Salidas_placebo,Salidas_placeboAdmin)
admin.site.register(Tratamientos,TratamientosAdmin)
admin.site.register(Patologias_grupo,Patologias_grupoAdmin)
admin.site.register(Patologias,PatologiasAdmin)
admin.site.register(Medicamentos_laboratorio,Medicamentos_laboratorioAdmin)
admin.site.register(Medicamentos_tipo,Medicamentos_tipoAdmin)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Medicamentos_indicacione,Medicamentos_indicacioneAdmin)
admin.site.register(animales_genetica,animales_geneticaAdmin)
admin.site.register(animale,animaleAdmin)
admin.site.register(mortalidad,mortalidadAdmin)
admin.site.register(Traslados_animale,Traslados_animaleAdmin)
admin.site.register(Traslados_alimento,Traslados_alimentoAdmin)
