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

urlpatterns = patterns('',

url(r'^', include(router.urls)),
url(r'^jet/', include('jet.urls', 'jet')),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^token-auth/$','rest_framework.authtoken.views.obtain_auth_token'),
url(r'^api/user', LoginView.as_view()),
url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
url(r'^admin/', include(admin.site.urls)),

)
