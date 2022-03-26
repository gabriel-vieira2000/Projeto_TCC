from django.urls import path

from site_controle_estoque_medicamentos.views import home, teste

urlpatterns = [
    path('', home),
    path('teste/', teste)
]
