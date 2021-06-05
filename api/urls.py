from django.urls import path

from api import views

urlpatterns = [
    # moneda
    path('get_moneda/<str:isocode>', views.get_moneda),
    path('get_moneda/', views.get_moneda),
    path('create_moneda', views.create_moneda),
    path('delete_moneda/<str:isocode>', views.delete_moneda),
    path('update_moneda', views.update_moneda),
    # tipo contacto
    path('get_tipo_contacto/<int:arg>', views.get_tipo_contacto),
    path('get_tipo_contacto/', views.get_tipo_contacto),
    path('create_tipo_contacto', views.create_tipo_contacto),
    path('delete_tipo_contacto/<int:arg>', views.delete_tipo_contacto),
    path('update_tipo_contacto', views.update_tipo_contacto),

    # proveedor
    path('get_proveedor/<int:arg>', views.get_proveedor),
    path('get_proveedor/', views.get_proveedor),
    path('create_proveedor', views.create_proveedor),
    path('delete_proveedor/<int:arg>', views.delete_proveedor),

    # estatus_proveedor
    path('get_estatus_proveedor/<int:arg>', views.get_estatus_proveedor),
    path('get_estatus_proveedor/', views.get_estatus_proveedor),
    path('create_estatus_proveedor', views.create_estatus_proveedor),
    path('delete_estatus_proveedor/<int:arg>', views.delete_estatus_proveedor),

    # contacto
    path('get_contacto/<int:arg>', views.get_contacto),
    path('get_contacto/', views.get_contacto),
    path('create_contacto', views.create_contacto),
    path('delete_contacto/<int:arg>', views.delete_contacto),

    # licitacion
    path('get_licitacion/<int:arg>', views.get_licitacion),
    path('get_licitacion/', views.get_licitacion),
    path('create_licitacion', views.create_licitacion),
    path('delete_licitacion/<int:arg>', views.delete_licitacion),

    # pais
    path('get_pais/<str:arg>', views.get_pais),
    path('get_pais/', views.get_pais),
    path('create_pais', views.create_pais),
    path('delete_pais/<str:arg>', views.delete_pais),
    path('update_pais', views.update_pais),

    # localidad
    path('get_localidad/<int:id>', views.get_localidad),
    path('get_localidad/', views.get_localidad),
    path('create_localidad', views.create_localidad),
    path('delete_localidad/<int:arg>', views.delete_localidad),

    # organismo
    path('get_organismo/<int:arg>', views.get_organismo),
    path('get_organismo/', views.get_organismo),
    path('create_organismo', views.create_organismo),
    path('delete_organismo/<int:arg>', views.delete_organismo),

    # ejecutivo
    path('get_ejecutivo/<int:arg>', views.get_ejecutivo),
    path('get_ejecutivo/', views.get_ejecutivo),
    path('create_ejecutivo', views.create_ejecutivo),
    path('delete_ejecutivo/<int:arg>', views.delete_ejecutivo),

    # rol
    path('get_rol/<int:arg>', views.get_rol),
    path('get_rol/', views.get_rol),
    path('create_rol', views.create_rol),
    path('delete_rol/<int:arg>', views.delete_rol),

    # rolEjecutivo
    path('get_rolEjecutivo/<int:arg>', views.get_rolEjecutivo),
    path('get_rolEjecutivo/', views.get_rolEjecutivo),
    path('create_rolEjecutivo', views.create_rolEjecutivo),
    path('delete_rolEjecutivo/<int:arg>', views.delete_rolEjecutivo),

    # proveedorEstatus_proveedor
    path('get_proveedorEstatus_proveedor/<int:arg>', views.get_proveedorEstatus_proveedor),
    path('get_proveedorEstatus_proveedor/', views.get_proveedorEstatus_proveedor),
    path('create_proveedorEstatus_proveedor', views.create_proveedorEstatus_proveedor),
    path('delete_proveedorEstatus_proveedor/<int:arg>', views.delete_proveedorEstatus_proveedor),

    # estadoProveedor_licitaciones
    path('get_estadoProveedor_licitacion/<str:arg>', views.get_estadoProveedor_licitacion),
    path('get_estadoProveedor_licitacion/', views.get_estadoProveedor_licitacion),
    path('create_estadoProveedor_licitacion', views.create_estadoProveedor_licitacion),
    path('delete_estadoProveedor_licitacion/<int:arg>', views.delete_estadoProveedor_licitacion),

    # proveedorLicitacion
    path('get_proveedorLicitacion/<str:arg>', views.get_proveedorLicitacion),
    path('get_proveedorLicitacion/', views.get_proveedorLicitacion),
    path('create_proveedorLicitacion', views.create_proveedorLicitacion),
    path('delete_proveedorLicitacion/<int:arg>', views.delete_proveedorLicitacion),

]
