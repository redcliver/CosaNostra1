from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.outros),
    url(r'^cadproduto/$', views.cadproduto),
    url(r'^cadservico/$', views.cadservico),
    ]