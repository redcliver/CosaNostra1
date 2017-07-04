from django.conf.urls import url
from . import views



urlpatterns = [

    url(r'^$', views.cortes),
    url(r'^imediato/$', views.imediato),
    url(r'^agendar/$', views.agendar),

    ]
