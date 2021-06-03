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
    # estatus_proveedor
    path('get_estatus_proveedor/<int:arg>', views.get_estatus_proveedor),
    path('get_estatus_proveedor/', views.get_estatus_proveedor),
    path('create_estatus_proveedor', views.create_estatus_proveedor),
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
    path('get_organismov<str:arg>', views.get_organismo),
    path('get_organismo/', views.get_organismo),
    path('create_organismo', views.create_organismo),
    # ejecutivo
    path('get_ejecutivo/<str:arg>', views.get_ejecutivo),
    path('get_ejecutivo/', views.get_ejecutivo),
    path('create_ejecutivo', views.create_ejecutivo),
    # rol
    path('get_rol/<str:arg>', views.get_rol),
    path('get_rol/', views.get_rol),
    path('create_rol', views.create_rol),
    # rolEjecutivo
    path('get_rolEjecutivo/<str:arg>', views.get_rolEjecutivo),
    path('get_rolEjecutivo/', views.get_rolEjecutivo),
    path('create_rolEjecutivo', views.create_rolEjecutivo),
    # proveedorEstatus_proveedor
    path('get_proveedorEstatus_proveedor/<str:arg>', views.get_proveedorEstatus_proveedor),
    path('get_proveedorEstatus_proveedor/', views.get_proveedorEstatus_proveedor),
    path('create_proveedorEstatus_proveedor', views.create_proveedorEstatus_proveedor),
    # estadoProveedor_licitaciones
    path('get_estadoProveedor_licitacion/<str:arg>', views.get_estadoProveedor_licitacion),
    path('get_estadoProveedor_licitacion/', views.get_estadoProveedor_licitacion),
    path('create_estadoProveedor_licitacion', views.create_estadoProveedor_licitacion),


]
