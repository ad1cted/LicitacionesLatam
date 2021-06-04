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
    isocode = models.ForeignKey(Pais, db_column='isocode', default=None, on_delete=models.CASCADE)


class Proveedor(TimeStampMixin):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)
    dni = models.CharField(unique=True, max_length=50, blank=True, null=True)
    id_localidad = models.ForeignKey(Localidad, blank=True, null=True, on_delete=models.CASCADE)
    fecha_inicio_actividades = models.DateTimeField(blank=True, null=True)


class EstatusProveedor(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True, unique=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)


class ProveedorEstatusProveedor(TimeStampMixin):
    raw_data = models.CharField(max_length=50, blank=True, null=True)
    id_EstatusProveedor = models.ForeignKey(EstatusProveedor, blank=True, null=True, on_delete=models.CASCADE)
    id_Proveedor = models.ForeignKey(Proveedor, blank=True, null=True, on_delete=models.CASCADE)


class TipoContacto(TimeStampMixin):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)


class Contacto(models.Model):
    valor = models.CharField(unique=True, max_length=50, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    id_Proveedor = models.ForeignKey(Proveedor, blank=True, null=True, on_delete=models.CASCADE)
    id_TipoContacto = models.ForeignKey(TipoContacto, blank=True, null=True, on_delete=models.CASCADE)


class EstadoProvedorLicitacion(TimeStampMixin):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)


class Organismo(TimeStampMixin):
    nombre = models.CharField(max_length=40, blank=True, null=True, unique=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    dni = models.CharField(max_length=30, blank=True, null=True)
    id_Localidad = models.ForeignKey(Localidad, blank=True, null=True, on_delete=models.CASCADE)


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
    id_Pais = models.ForeignKey(Pais, on_delete=models.CASCADE, blank=True, null=True)
    id_Moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE, blank=True, null=True)
    id_Organismo = models.ForeignKey(Organismo, blank=True, null=True, on_delete=models.CASCADE)
    id_Ejecutivo = models.ForeignKey(Ejecutivo, blank=True, null=True, on_delete=models.CASCADE)


class ProveedorLicitacion(TimeStampMixin):
    raw_data = models.TextField(blank=True, null=True)
    id_Licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE, blank=True, null=True)
    id_EstadoProvedorLicitacion = models.ForeignKey(EstadoProvedorLicitacion, on_delete=models.CASCADE, blank=True,
                                                    null=True)
    id_Proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=True, null=True)


class Rol(TimeStampMixin):
    nombre = models.CharField(unique=True, max_length=20, blank=True, null=True)
    configuracion = models.JSONField()


class RolEjecutivo(TimeStampMixin):
    id_Rol = models.ForeignKey(Rol, on_delete=models.CASCADE, blank=True, null=True)
    id_Ejecutivo = models.ForeignKey(Ejecutivo, on_delete=models.CASCADE, blank=True, null=True)
