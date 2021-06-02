from django.urls import path
from api import views

urlpatterns = [
    # moneda
    path('get_moneda/<str:arg>', views.get_moneda),
    path('get_moneda/', views.get_moneda),
    path('create_moneda', views.create_moneda),
    # tipo contacto
    path('get_tipo_contacto/<int:arg>', views.get_tipo_contacto),
    path('get_tipo_contacto/', views.get_tipo_contacto),
    path('create_tipo_contacto', views.create_tipo_contacto),
    #proveedor
    path('get_proveedor/<int:arg>', views.get_proveedor),
    path('get_proveedor/', views.get_proveedor),
    path('create_proveedor', views.create_proveedor),
    # status_proveedor
    path('get_status_proveedor/<int:arg>', views.get_status_proveedor),
    path('get_status_proveedor/', views.get_status_proveedor),
    path('create_status_proveedor', views.create_status_proveedor),
    #contacto
    path('get_contacto/<int:arg>', views.get_contacto),
    path('get_contacto/', views.get_contacto),
    path('create_contacto', views.create_contacto),
    # licitacion
    path('get_licitacion/<int:arg>', views.get_licitacion),
    path('get_licitacion/', views.get_licitacion),
    path('create_licitacion', views.create_licitacion),
    # pais
    path('get_pais/<str:arg>', views.get_pais),
    path('get_pais/', views.get_pais),
    path('create_pais', views.create_pais),
    # pais
    path('get_localidad/<str:arg>', views.get_localidad),
    path('get_localidad/', views.get_localidad),
    path('create_localidad', views.create_localidad),
    # organismo
    path('get_organismo<str:arg>', views.get_organismo),
    path('get_organismo/', views.get_organismo),
    path('create_organismo', views.create_organismo),
    # ejecutivo
    path('get_ejecutivo<str:arg>', views.get_ejecutivo),
    path('get_ejecutivo/', views.get_ejecutivo),
    path('create_ejecutivo', views.create_ejecutivo),
]
