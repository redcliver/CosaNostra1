from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.vendas),
    url(r'^imediato/$', views.imediato),
    url(r'^bar/$', views.bar),

    ]
