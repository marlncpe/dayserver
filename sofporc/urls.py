from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from website.viewsets import *
from website.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()


urlpatterns = patterns('',

url(r'^', include(router.urls)),

url(r'^admin/', include(admin.site.urls)),

)
