from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.clientes),
    url(r'^addcliente/$', views.addcliente),
    url(r'^buscacli/$', views.buscacli),
    ]
