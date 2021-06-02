from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        managed = True



class Pais(TimeStampMixin):
    isocode = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)


class Localidad(TimeStampMixin):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    codigo_area = models.IntegerField()
    isocode = models.ForeignKey(Pais, models.DO_NOTHING, db_column='isocode', default=None)


class Proveedor(TimeStampMixin):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)
    dni = models.CharField(unique=True, max_length=50, blank=True, null=True)
    id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, blank=True, null=True)
    fecha_inicio_actividades = models.DateTimeField(blank=True, null=True)


class EstatusProveedor(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True, unique=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)


class ProveedorEstatusProveedor(TimeStampMixin):
    raw_data = models.CharField(max_length=50, blank=True, null=True)
    id_EstatusProveedor = models.ForeignKey(EstatusProveedor, models.DO_NOTHING, blank=True, null=True)
    id_Proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)


class TipoContacto(TimeStampMixin):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)


class Contacto(models.Model):
    valor = models.CharField(unique=True, max_length=50, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_Proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    id_TipoContacto = models.ForeignKey(TipoContacto, models.DO_NOTHING, blank=True, null=True)


class EstadoProvedorLicitacion(TimeStampMixin):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)


class Organismo(TimeStampMixin):
    nombre = models.CharField(max_length=40, blank=True, null=True, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=30, blank=True, null=True)
    id_Localidad = models.ForeignKey(Localidad, models.DO_NOTHING, blank=True, null=True)


class Moneda(TimeStampMixin):
    isocode = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)


class Ejecutivo(TimeStampMixin):
    id_externo = models.IntegerField()
    username = models.CharField(max_length=20, blank=True, null=True, unique=True)
    activo = models.BooleanField(blank=True, null=True)


class Licitacion(TimeStampMixin):
    external_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)
    fecha_licitacion = models.DateTimeField(blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    importe_contrato = models.FloatField(blank=True, null=True)
    id_Pais = models.ForeignKey(Pais, models.DO_NOTHING, blank=True, null=True)
    id_Moneda = models.ForeignKey(Moneda, models.DO_NOTHING, blank=True, null=True)
    id_Organismo = models.ForeignKey(Organismo, models.DO_NOTHING, blank=True, null=True)
    id_Ejecutivo = models.ForeignKey(Ejecutivo, models.DO_NOTHING, blank=True, null=True)


class ProveedorLicitacion(TimeStampMixin):
    raw_data = models.TextField(blank=True, null=True)
    id_Licitacion = models.ForeignKey(Licitacion, models.DO_NOTHING, blank=True, null=True)
    id_EstadoProvedorLicitacion = models.ForeignKey(EstadoProvedorLicitacion, models.DO_NOTHING, blank=True, null=True)
    id_Proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)


class Rol(TimeStampMixin):
    nombre = models.CharField(unique=True, max_length=20, blank=True, null=True)
    configuracion = models.JSONField()


class RolEjecutivo(TimeStampMixin):
    id_Rol = models.ForeignKey(Rol, models.DO_NOTHING, blank=True, null=True)
    id_Ejecutivo = models.ForeignKey(Ejecutivo, models.DO_NOTHING, blank=True, null=True)
