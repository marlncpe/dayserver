from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from website.viewsets import *
from website.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'status', StatusViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'granjastipos', Granjas_tipoViewSet)
router.register(r'granjas', GranjaViewSet)
router.register(r'galpones', GalponeViewSet)
router.register(r'corrales', CorraleViewSet)
router.register(r'inmunocastraciones', InmunocastracioneViewSet)
router.register(r'inmunocastracionesextendida', Inmunocastraciones_extendidaViewSet)
router.register(r'alimentosfabrica', Alimentos_fabricaViewSet)
router.register(r'alimentosfase', Alimentos_faseViewSet)
router.register(r'alimentostipo', Alimentos_tipoViewSet)
router.register(r'alimentos', AlimentoViewSet)
router.register(r'patologiasgrupo', Patologias_grupoViewSet)
router.register(r'patologias', PatologiasViewSet)
router.register(r'medicamentoslaboratorio', Medicamentos_laboratorioViewSet)
router.register(r'medicamentostipo', Medicamentos_tipoViewSet)
router.register(r'medicamentosindicaciones', Medicamentos_indicacioneViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'Manoobrastipo', Mano_obras_tipoViewSet)
router.register(r'Manoobras', Mano_obraViewSet)
router.register(r'personal', personalViewSet)
router.register(r'insumos', InsumoViewSet)

urlpatterns = patterns('',

url(r'^', include(router.urls)),
url(r'^jet/', include('jet.urls', 'jet')),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^token-auth/$','rest_framework.authtoken.views.obtain_auth_token'),
url(r'^api/user', LoginView.as_view()),
url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
url(r'^admin/', include(admin.site.urls)),

)
