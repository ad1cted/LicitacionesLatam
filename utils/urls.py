from django.urls import path
from utils.utils.views import *
urlpatterns = [
    path('get_datos_contactabilidad/<str:pais>/<str:empresa>', deriva_datos_contacto),
    path('get_datos_licitacion/<str:pais>/<int:id_externo>', deriva_datos_licitacion),
    path('get_proveedor_sancionado/<str:pais>/<int:dni>', deriva_proveedor_sancionado)



]
