from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from website.viewsets import *
from granjas.viewsets import *
from capturedatos.viewsets import *
from website.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'status', StatusViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'granjas/tipos', Granjas_tipoViewSet)
router.register(r'granjas', GranjaViewSet)
router.register(r'galpones', GalponeViewSet)
router.register(r'corrales', CorraleViewSet)
router.register(r'inmunocastraciones', InmunocastracioneViewSet)
router.register(r'inmunocastraciones/extendida', Inmunocastraciones_extendidaViewSet)
router.register(r'alimentos/fabrica', Alimentos_fabricaViewSet)
router.register(r'alimentos/fase', Alimentos_faseViewSet)
router.register(r'alimentos/tipo', Alimentos_tipoViewSet)
router.register(r'alimentos', AlimentoViewSet)
router.register(r'patologiasgrupo', Patologias_grupoViewSet)
router.register(r'patologias', PatologiasViewSet)
router.register(r'medicamentos/laboratorio', Medicamentos_laboratorioViewSet)
router.register(r'medicamentos/tipo', Medicamentos_tipoViewSet)
router.register(r'medicamentos/indicaciones', Medicamentos_indicacioneViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'Manoobras/tipo', Mano_obras_tipoViewSet)
router.register(r'Manoobras', Mano_obraViewSet)
router.register(r'personal', personalViewSet)
router.register(r'insumos', InsumoViewSet)
router.register(r'pedidostipo', Pedidos_tipoViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'pedidos/medicamentos', pedidos_medicamentos_extendidoViewSet)
router.register(r'pedidos/alimentos', pedidos_alimentos_extendidoViewSet)
router.register(r'animales/genetica', animales_geneticaViewSet)
router.register(r'animales', animaleViewSet)
router.register(r'mortalidad', mortalidadViewSet)
router.register(r'compras/tipos', Compras_tipoViewSet)
router.register(r'compras', CompraViewSet)
router.register(r'compras/insumos', Compras_insumoViewSet)
router.register(r'compras/medicamentos', Compras_medicamentoViewSet)
router.register(r'compras/alimentos', Compras_alimentoViewSet)
router.register(r'medicado', MedicadoViewSet)
router.register(r'traslado/alimentos', Traslados_alimentoViewSet)
router.register(r'traslado/animales', Traslados_animaleViewSet)
router.register(r'ventas', ventasViewSet)
router.register(r'costos', Costos_gastoViewSet)
router.register(r'consumo/tipo', Consumos_tipoViewSet)
router.register(r'consumo/farmaco', Consumos_farmacoViewSet)
router.register(r'consumo/insumo', Consumos_insumoViewSet)
router.register(r'consumo/alimento', Consumos_alimentoViewSet)
router.register(r'consumo', ConsumoViewSet)
router.register(r'salidas/placebo', Salidas_placeboViewSet)
router.register(r'tratamientos', TratamientosViewSet)
router.register(r'curvas/crecimiento', Curvas_crecimientoViewSet)
router.register(r'metas/pc', Metas_pcViewSet)
router.register(r'metas/ceba', Metas_cebaViewSet)
router.register(r'metas/destete', Metas_destete_finalizacioneViewSet)

router.register(r'metas/recordatorio', RecordatorioViewSet)
router.register(r'metas/recordatorio/extendido', Recordatorios_extendidoViewSet)
urlpatterns = patterns('',

url(r'^', include(router.urls)),
url(r'^jet/', include('jet.urls', 'jet')),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^token-auth/$','rest_framework.authtoken.views.obtain_auth_token'),
url(r'^api/user', LoginView.as_view()),
url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
url(r'^admin/', include(admin.site.urls)),
url(r'^rest-auth/', include('rest_auth.urls'))

)
