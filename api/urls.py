from django.urls import path
from api import views

urlpatterns = [
    # moneda
    path('get_moneda/<str:arg>', views.get_moneda),
    path('get_moneda/', views.get_moneda),
    path('create_moneda', views.create_moneda),
    # tipo_codigo_nacional
    path('get_tipo_codigo_nacional/<int:arg>', views.get_tipo_codigo_nacional),
    path('get_tipo_codigo_nacional/', views.get_tipo_codigo_nacional),
    path('create_tipo_codigo_nacional', views.create_tipo_codigo_nacional),
    # tipo contacto
    path('get_tipo_contacto/<int:arg>', views.get_tipo_contacto),
    path('get_tipo_contacto/', views.get_tipo_contacto),
    path('create_tipo_contacto', views.create_tipo_contacto),
    #proveedor
    path('get_proveedor/<int:arg>', views.get_proveedor),
    path('get_proveedor/', views.get_proveedor),
    path('create_proveedor', views.create_proveedor),
    #status_adjudicacion
    path('get_status_adjudicacion/<int:arg>', views.get_status_adjudicacion),
    path('get_status_adjudicacion/', views.get_status_adjudicacion),
    path('create_status_adjudicacion', views.create_status_adjudicacion),
    # status_proveedor
    path('get_status_proveedor/<int:arg>', views.get_status_proveedor),
    path('get_status_proveedor/', views.get_status_proveedor),
    path('create_status_proveedor', views.create_status_proveedor),
    #estatus_licitacion
    path('get_status_licitacion/<int:arg>', views.get_status_licitacion),
    path('get_status_licitacion/', views.get_status_licitacion),
    path('create_status_licitacion', views.create_status_licitacion),
    # codigo_categorio
    path('get_codigo_categoria/<int:arg>', views.get_codigo_categoria),
    path('get_codigo_categoria/', views.get_codigo_categoria),
    path('create_codigo_categoria', views.create_codigo_categoria),
    #contacto
    path('get_contacto/<int:arg>', views.get_contacto),
    path('get_contacto/', views.get_contacto),
    path('create_contacto', views.create_contacto),
    # licitacion
    path('get_licitacion/<int:arg>', views.get_licitacion),
    path('get_licitacion/', views.get_licitacion),
    path('create_licitacion', views.create_licitacion),
    #adjudicacion
    path('get_adjudicacion/<int:arg>', views.get_adjudicacion),
    path('get_adjudicacion/', views.get_adjudicacion),
    path('create_adjudicacion', views.create_adjudicacion),
    # licitante
    path('get_licitante/<int:arg>', views.get_licitante),
    path('get_licitante/', views.get_licitante),
    path('create_licitante', views.create_licitante),
]
