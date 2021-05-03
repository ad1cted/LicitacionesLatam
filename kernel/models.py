from django.db import models


class Adjudicacion(models.Model):
    id_adjudicacion = models.IntegerField(primary_key=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    id_licitacion = models.ForeignKey('Licitacion', models.DO_NOTHING, db_column='id_licitacion', blank=True, null=True)
    importe_contrato = models.CharField(max_length=50, blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)
    id_status_adjudicacion = models.ForeignKey('StatusAdjudicacion', models.DO_NOTHING,
                                               db_column='id_status_adjudicacion', blank=True, null=True)


class CodigoCategoria(models.Model):
    id_codigo_categoria = models.IntegerField(primary_key=True)
    codigo_nacional = models.CharField(max_length=50, blank=True, null=True)
    codigo_onu = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    tipo_codigo_nacional = models.ForeignKey('TipoCodigoNacional', models.DO_NOTHING, db_column='tipo_codigo_nacional',
                                             blank=True, null=True)


class Contacto(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    descripcion = models.CharField(unique=True, max_length=50, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor', blank=True, null=True)
    id_tipo_contacto = models.ForeignKey('TipoContacto', models.DO_NOTHING, db_column='id_tipo_contacto', blank=True,
                                         null=True)


class EstadoLicitacion(models.Model):
    id_estado_licitacion = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)


class EstadoProveedor(models.Model):
    id_estado_proveedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)


class Licitacion(models.Model):
    id_licitacion = models.AutoField(primary_key=True)
    external_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    raw_data = models.CharField(max_length=50, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    fecha_publicacion = models.CharField(max_length=50, blank=True, null=True)
    fecha_apertura = models.CharField(max_length=50, blank=True, null=True)
    cod_country = models.CharField(max_length=50, blank=True, null=True)
    origen = models.CharField(max_length=50, blank=True, null=True)
    isocode = models.ForeignKey('Moneda', models.DO_NOTHING, db_column='isocode', blank=True, null=True)
    id_licitante = models.ForeignKey('Licitante', models.DO_NOTHING, db_column='id_licitante', blank=True, null=True)
    id_estado_licitacion = models.ForeignKey(EstadoLicitacion, models.DO_NOTHING, db_column='id_estado_licitacion', blank=True, null=True)
    pushed = models.BooleanField(blank=True, null=True)


class Licitante(models.Model):
    id_licitante = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    siglas = models.CharField(max_length=50, blank=True, null=True)
    raw_data = models.CharField(max_length=50, blank=True, null=True)


class Moneda(models.Model):
    isocode = models.CharField(primary_key=True, max_length=50)
    nombre = models.CharField(max_length=50, blank=True, null=True)


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    grado_cumplimiento = models.CharField(max_length=50, blank=True, null=True)
    estratificacion = models.CharField(max_length=50, blank=True, null=True)
    cod_country = models.CharField(max_length=50, blank=True, null=True)
    raw_data = models.CharField(max_length=50, blank=True, null=True)
    dni = models.CharField(unique=True, max_length=50, blank=True, null=True)
    id_estado_proveedor = models.ForeignKey(EstadoProveedor, models.DO_NOTHING, db_column='id_estado_proveedor', blank=True, null=True)
    raw_giro = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)


class StatusAdjudicacion(models.Model):
    id_status_adjudicacion = models.AutoField(primary_key=True)
    nombre_status_adjudicacion = models.CharField(max_length=50)
    descripcion_status_adjudicacion = models.CharField(max_length=50, blank=True, null=True)


class HistoricalStatusAssign(models.Model):
    id_historical_status_assing = models.AutoField(primary_key=True)
    id_status_adjudicacion = models.ForeignKey(StatusAdjudicacion, models.DO_NOTHING, db_column='id_status_adjudicacion', blank=True, null=True)
    id_adjudicacion = models.ForeignKey(Adjudicacion, models.DO_NOTHING, db_column='id_adjudicacion', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)


class TipoCodigoNacional(models.Model):
    id_tipo_codigo_nacional = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    cod_country = models.CharField(max_length=50, blank=True, null=True)


class TipoContacto(models.Model):
    id_tipo_contacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
