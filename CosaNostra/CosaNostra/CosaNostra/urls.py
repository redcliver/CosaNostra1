"""
Definition of urls for CosaNostra.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^cortes/', include('cortes.urls')),
    url(r'^vendas/', include('vendas.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^agenda/', include('agenda.urls')),
    url(r'^caixa/', include('caixa.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
