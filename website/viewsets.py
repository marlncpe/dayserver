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
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('username',)

class StatusViewSet(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    permission_classes = [permissions.AllowAny,]
'''
class Granjas_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Granjas_tipoSerializer
    queryset = Granjas_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class GranjaViewSet(viewsets.ModelViewSet):
    serializer_class = GranjaSerializer
    queryset = Granja.objects.all()
    permission_classes = [permissions.AllowAny,]
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('nombre','dueno__id')

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
'''
class Alimentos_fabricaViewSet(viewsets.ModelViewSet):
    serializer_class = Alimentos_fabricaSerializer
    queryset = Alimentos_fabrica.objects.all()
    permission_classes = [permissions.AllowAny,]

class Alimentos_faseViewSet(viewsets.ModelViewSet):
    serializer_class = Alimentos_faseSerializer
    queryset = Alimentos_fase.objects.all()
    permission_classes = [permissions.AllowAny,]

class Alimentos_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Alimentos_tipoSerializer
    queryset = Alimentos_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class AlimentoViewSet(viewsets.ModelViewSet):
    serializer_class = AlimentoSerializer
    queryset = Alimento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Mano_obras_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Mano_obras_tipoSerializer
    queryset = Mano_obras_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class Mano_obraViewSet(viewsets.ModelViewSet):
    serializer_class = Mano_obraSerializer
    queryset = Mano_obra.objects.all()
    permission_classes = [permissions.AllowAny,]

class personalViewSet(viewsets.ModelViewSet):
    serializer_class = personalSerializer
    queryset = personal.objects.all()
    permission_classes = [permissions.AllowAny,]

class InsumoViewSet(viewsets.ModelViewSet):
    serializer_class = InsumoSerializer
    queryset = Insumo.objects.all()
    permission_classes = [permissions.AllowAny,]
    
class Pedidos_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Pedidos_tipoSerializer
    queryset = Pedidos_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny,]

class pedidos_medicamentos_extendidoViewSet(viewsets.ModelViewSet):
    serializer_class = pedidos_medicamentos_extendidoSerializer
    queryset = pedidos_medicamentos_extendido.objects.all()
    permission_classes = [permissions.AllowAny,]

class pedidos_alimentos_extendidoViewSet(viewsets.ModelViewSet):
    serializer_class = pedidos_alimentos_extendidoSerializer
    queryset = pedidos_alimentos_extendido.objects.all()
    permission_classes = [permissions.AllowAny,]

class Compras_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Compras_tipoSerializer
    queryset = Compras_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class CompraViewSet(viewsets.ModelViewSet):
    serializer_class = CompraSerializer
    queryset = Compra.objects.all()
    permission_classes = [permissions.AllowAny,]

class Compras_insumoViewSet(viewsets.ModelViewSet):
    serializer_class = Compras_insumoSerializer
    queryset = Compras_insumo.objects.all()
    permission_classes = [permissions.AllowAny,]

class Compras_medicamentoViewSet(viewsets.ModelViewSet):
    serializer_class = Compras_medicamentoSerializer
    queryset = Compras_medicamento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Compras_alimentoViewSet(viewsets.ModelViewSet):
    serializer_class = Compras_alimentoSerializer
    queryset = Compras_alimento.objects.all()
    permission_classes = [permissions.AllowAny,]

class MedicadoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicadoSerializer
    queryset = Medicado.objects.all()
    permission_classes = [permissions.AllowAny,]
    
class ventasViewSet(viewsets.ModelViewSet):
    serializer_class = ventasSerializer
    queryset = ventas.objects.all()
    permission_classes = [permissions.AllowAny,]

class Costos_gastoViewSet(viewsets.ModelViewSet):
    serializer_class = Costos_gastoSerializer
    queryset = Costos_gasto.objects.all()
    permission_classes = [permissions.AllowAny,]

class Consumos_tipoViewSet(viewsets.ModelViewSet):
    serializer_class = Consumos_tipoSerializer
    queryset = Consumos_tipo.objects.all()
    permission_classes = [permissions.AllowAny,]

class ConsumoViewSet(viewsets.ModelViewSet):
    serializer_class = ConsumoSerializer
    queryset = Consumo.objects.all()
    permission_classes = [permissions.AllowAny,]

class Consumos_farmacoViewSet(viewsets.ModelViewSet):
    serializer_class = Consumos_farmacoSerializer
    queryset = Consumos_farmaco.objects.all()
    permission_classes = [permissions.AllowAny,]

class Consumos_alimentoViewSet(viewsets.ModelViewSet):
    serializer_class = Consumos_alimentoSerializer
    queryset = Consumos_alimento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Consumos_insumoViewSet(viewsets.ModelViewSet):
    serializer_class = Consumos_insumoSerializer
    queryset = Consumos_insumo.objects.all()
    permission_classes = [permissions.AllowAny,]       

class Curvas_crecimientoViewSet(viewsets.ModelViewSet):
    serializer_class = Curvas_crecimientoSerializer
    queryset = Curvas_crecimiento.objects.all()
    permission_classes = [permissions.AllowAny,]

class Metas_pcViewSet(viewsets.ModelViewSet):
    serializer_class = Metas_pcSerializer
    queryset = Metas_pc.objects.all()
    permission_classes = [permissions.AllowAny,]

class Metas_cebaViewSet(viewsets.ModelViewSet):
    serializer_class = Metas_cebaSerializer
    queryset = Metas_ceba.objects.all()
    permission_classes = [permissions.AllowAny,]

class Metas_destete_finalizacioneViewSet(viewsets.ModelViewSet):
    serializer_class = Metas_destete_finalizacioneSerializer
    queryset = Metas_destete_finalizacione.objects.all()
    permission_classes = [permissions.AllowAny,]

class RecordatorioViewSet(viewsets.ModelViewSet):
    serializer_class = RecordatorioSerializer
    queryset = Recordatorio.objects.all()
    permission_classes = [permissions.AllowAny,]

class Recordatorios_extendidoViewSet(viewsets.ModelViewSet):
    serializer_class = Recordatorios_extendidoSerializer
    queryset = Recordatorios_extendido.objects.all()
    permission_classes = [permissions.AllowAny,]

'''
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
'''