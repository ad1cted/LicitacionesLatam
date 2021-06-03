from django.urls import path
from utils.utils.views.MEX.views import get_denue, get_data_by_codigo_expediente, get_data_by_opportunity_id

urlpatterns = [
    path('get_denue', get_denue),
    path('get_data_by_codigo_expediente', get_data_by_codigo_expediente),
    path('get_data_by_opportunity_id', get_data_by_opportunity_id)
]
