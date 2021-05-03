from rest_framework import serializers
from kernel.models import Moneda, TipoCodigoNacional, TipoContacto, Proveedor, StatusAdjudicacion, \
    EstadoProveedor, EstadoLicitacion, CodigoCategoria, Contacto, Adjudicacion, Licitacion, Licitante, HistoricalStatusAssign


class MonedaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Moneda
        fields = '__all__'


class TipoCodigoNacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCodigoNacional
        fields = '__all__'


class TipoContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContacto
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class StatusAdjudicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAdjudicacion
        fields = '__all__'


class EstadoProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoProveedor
        fields = '__all__'


class EstadoLicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoLicitacion
        fields = '__all__'


class CodigoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoCategoria
        fields = '__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'


class AdjudicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adjudicacion
        fields = '__all__'


class LicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacion
        fields = '__all__'


class LicitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitante
        fields = '__all__'


class HistoricalStatusAssignSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalStatusAssign
        fields = '__all__'
