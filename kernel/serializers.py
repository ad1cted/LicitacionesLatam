from rest_framework import serializers

from kernel.models import Moneda, TipoContacto, Proveedor, \
    EstatusProveedor, Contacto, Licitacion, Pais, Localidad, Organismo, Ejecutivo, Rol, RolEjecutivo, \
    ProveedorEstatusProveedor, EstadoProvedorLicitacion, ProveedorLicitacion, Portafolio, TipoLicitacion


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = '__all__'


class TipoContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContacto
        fields = '__all__'


class OrganismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organismo
        fields = '__all__'


class EjecutivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejecutivo
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'


class RolEjecutivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolEjecutivo
        fields = '__all__'


class EstatusProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusProveedor
        fields = '__all__'


class ProveedorEstatusProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorEstatusProveedor
        fields = '__all__'


class EstadoProvedorLicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoProvedorLicitacion
        fields = '__all__'


class ProveedorLicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProveedorLicitacion
        fields = '__all__'


class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = '__all__'


class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'


class LicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licitacion
        fields = '__all__'


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'


class PortafolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portafolio
        fields = '__all__'


class TipoLicitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLicitacion
        fields = '__all__'
