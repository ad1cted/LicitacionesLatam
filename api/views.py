from kernel.models import Moneda, TipoCodigoNacional, TipoContacto, Proveedor, StatusAdjudicacion, \
    EstadoProveedor, EstadoLicitacion, CodigoCategoria, Contacto, Adjudicacion, Licitacion, Licitante, HistoricalStatusAssign
from kernel.serializers import MonedaSerializer, TipoCodigoNacionalSerializer, TipoContactoSerializer, ProveedorSerializer, \
    StatusAdjudicacionSerializer, EstadoProveedorSerializer, EstadoLicitacionSerializer, CodigoCategoriaSerializer, \
    ContactoSerializer, AdjudicacionSerializer, LicitacionSerializer, LicitanteSerializer, HistoricalStatusAssign
from django.core.handlers.wsgi import WSGIRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import json


# moneda
@api_view(['GET'])
def get_moneda(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        monedas: list = [Moneda.objects.get(isocode=arg)]
    else:
        monedas: list = Moneda.objects.all()
    serializer: MonedaSerializer = MonedaSerializer(monedas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_moneda(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    isocode: str = body.get("isocode", None)
    nombre: str = body.get("nombre", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if isocode and nombre:
        Moneda.objects.create(isocode=isocode, nombre=nombre)
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# codigo nacional
@api_view(['GET'])
def get_tipo_codigo_nacional(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            tipo_codigo_nacional: list = [TipoCodigoNacional.objects.get(id_tipo_codigo_nacional=arg)]
        except ObjectDoesNotExist:
            tipo_codigo_nacional = []
    else:
        tipo_codigo_nacional: list = TipoCodigoNacional.objects.all()
    serializer: TipoCodigoNacionalSerializer = TipoCodigoNacionalSerializer(tipo_codigo_nacional, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_tipo_codigo_nacional(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    cod_country: str = body.get("cod_country", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre and cod_country:
        TipoCodigoNacional.objects.create(descripcion=descripcion, nombre=nombre, cod_country=cod_country)
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# tipo contacto
@api_view(['GET'])
def get_tipo_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            tipo_contacto: list = [TipoContacto.objects.get(id_tipo_contacto=arg)]
        except ObjectDoesNotExist:
            tipo_contacto = []
    else:
        tipo_contacto: list = TipoContacto.objects.all()
    serializer: TipoContactoSerializer = TipoContactoSerializer(tipo_contacto, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_tipo_contacto(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        TipoContacto.objects.create(nombre=nombre)
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# proveedor
@api_view(['GET'])
def get_proveedor(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            proveedor: list = [Proveedor.objects.get(id_proveedor=arg)]
        except ObjectDoesNotExist:
            proveedor = []
    else:
        proveedor: list = Proveedor.objects.all()
    serializer: ProveedorSerializer = ProveedorSerializer(proveedor, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_proveedor(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    razon_social: str = body.get("razon_social", None)
    descripcion: str = body.get("descripcion", None)
    grado_cumplimiento: str = body.get("grado_cumplimiento", None)
    estratificacion: str = body.get("estratificacion", None)
    cod_country: str = body.get("cod_country", None)
    raw_data: str = body.get("raw_data", None)
    dni: str = body.get("dni", None)
    id_estado_proveedor: int = body.get("id_estado_proveedor", None)
    raw_giro: str = body.get("raw_giro", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        Proveedor.objects.create(
            nombre=nombre,
            razon_social=razon_social,
            descripcion=descripcion,
            grado_cumplimiento=grado_cumplimiento,
            estratificacion=estratificacion,
            cod_country=cod_country,
            raw_data=raw_data,
            dni=dni,
            id_estado_proveedor=EstadoProveedor.objects.get(id_estado_proveedor=id_estado_proveedor),
            raw_giro=raw_giro
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# status_djudicacion
@api_view(['GET'])
def get_status_adjudicacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            status_adjudicacion: list = [StatusAdjudicacion.objects.get(id_status_adjudicacion=arg)]
        except ObjectDoesNotExist:
            status_adjudicacion = []
    else:
        status_adjudicacion: list = StatusAdjudicacion.objects.all()
    serializer: StatusAdjudicacionSerializer = StatusAdjudicacionSerializer(status_adjudicacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_status_adjudicacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre_status_adjudicacion: str = body.get("nombre_status_adjudicacion", None)
    descripcion_status_adjudicacion: str = body.get("descripcion_status_adjudicacion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre_status_adjudicacion:
        StatusAdjudicacion.objects.create(
            nombre_status_adjudicacion=nombre_status_adjudicacion,
            descripcion_status_adjudicacion=descripcion_status_adjudicacion,
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# status_proveedor
@api_view(['GET'])
def get_status_proveedor(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            status_proveedor: list = [EstadoProveedor.objects.get(id_estado_proveedor=arg)]
        except ObjectDoesNotExist:
            status_proveedor = []
    else:
        status_proveedor: list = EstadoProveedor.objects.all()
    serializer: EstadoProveedorSerializer = EstadoProveedorSerializer(status_proveedor, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_status_proveedor(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        EstadoProveedor.objects.create(
            nombre=nombre,
            descripcion=descripcion,
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# status_licitacion
@api_view(['GET'])
def get_status_licitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            status_licitacion: list = [EstadoLicitacion.objects.get(id_estado_licitacion=arg)]
        except ObjectDoesNotExist:
            status_licitacion = []
    else:
        status_licitacion: list = EstadoLicitacion.objects.all()
    serializer: EstadoLicitacionSerializer = EstadoLicitacionSerializer(status_licitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_status_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        EstadoLicitacion.objects.create(
            nombre=nombre,
            descripcion=descripcion,
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# codigo_categoria
@api_view(['GET'])
def get_codigo_categoria(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            codigo_categoria: list = [CodigoCategoria.objects.get(id_codigo_categoria=arg)]
        except ObjectDoesNotExist:
            codigo_categoria = []
    else:
        codigo_categoria: list = CodigoCategoria.objects.all()
    serializer: CodigoCategoriaSerializer = CodigoCategoriaSerializer(codigo_categoria, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_codigo_categoria(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    codigo_nacional: str = body.get("codigo_nacional", None)
    codigo_onu: str = body.get("codigo_onu", None)
    descripcion: str = body.get("descripcion", None)
    id_tipo_codigo_nacional: int = body.get("id_tipo_codigo_nacional", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if codigo_nacional and id_tipo_codigo_nacional:
        CodigoCategoria.objects.create(
            codigo_nacional=codigo_nacional,
            codigo_onu=codigo_onu,
            descripcion=descripcion,
            tipo_codigo_nacional=TipoCodigoNacional.objects.get(id_tipo_codigo_nacional=id_tipo_codigo_nacional)
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# contacto
@api_view(['GET'])
def get_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            contacto: list = [Contacto.objects.get(id_contacto=arg)]
        except ObjectDoesNotExist:
            contacto = []
    else:
        contacto: list = Contacto.objects.all()
    serializer: ContactoSerializer = ContactoSerializer(contacto, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_contacto(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    descripcion: str = body.get("descripcion", None)
    activo: bool = body.get("activo", None)
    id_proveedor: int = body.get("id_proveedor", None)
    id_tipo_contacto: int = body.get("id_tipo_contacto", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if id_proveedor and id_tipo_contacto and descripcion:
        Contacto.objects.create(
            descripcion=descripcion,
            activo=activo,
            id_proveedor=Proveedor.objects.get(id_proveedor=id_proveedor),
            id_tipo_contacto=TipoContacto.objects.get(id_tipo_contacto=id_tipo_contacto)
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# adjudicacion
@api_view(['GET'])
def get_adjudicacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            adjudicacion: list = [Adjudicacion.objects.get(id_adjudicacion=arg)]
        except ObjectDoesNotExist:
            adjudicacion = []
    else:
        adjudicacion: list = Adjudicacion.objects.all()
    serializer: AdjudicacionSerializer = AdjudicacionSerializer(adjudicacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_adjudicacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    fecha_creacion: str = body.get("fecha_creacion", None)
    id_proveedor: bool = body.get("id_proveedor", None)
    id_licitacion: int = body.get("id_licitacion", None)
    importe_contrato: int = body.get("importe_contrato", None)
    titulo: int = body.get("titulo", None)
    id_status_adjudicacion: int = body.get("id_status_adjudicacion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if id_proveedor and id_licitacion and id_status_adjudicacion and titulo:
        Adjudicacion.objects.create(
            fecha_creacion=fecha_creacion,
            id_proveedor=Proveedor.objects.get(id_proveedor=id_proveedor),
            id_licitacion=Licitacion.objects.get(id_licitacion=id_licitacion),
            importe_contrato=importe_contrato,
            titulo=titulo,
            id_status_adjudicacion=StatusAdjudicacion.objects.get(id_status_adjudicacion=id_status_adjudicacion))
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# licitacion
@api_view(['GET'])
def get_licitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            licitacion: list = [Licitacion.objects.get(id_licitacion=arg)]
        except ObjectDoesNotExist:
            licitacion = []
    else:
        licitacion: list = Licitacion.objects.all()
    serializer: LicitacionSerializer = LicitacionSerializer(licitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    external_id: str = body.get("external_id", None)
    raw_data: str = body.get("raw_data", None)
    nombre: str = body.get("nombre", None)
    fecha_publicacion: str = body.get("fecha_publicacion", None)
    fecha_apertura: str = body.get("fecha_apertura", None)
    cod_country: str = body.get("cod_country", None)
    origen: str = body.get("origen", None)
    isocode: str = body.get("isocode", None)
    id_licitante: str = body.get("id_licitante", None)
    id_estado_licitacion: str = body.get("id_estado_licitacion", None)
    pushed: bool = body.get("pushed", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre and isocode and id_estado_licitacion:
        Licitacion.objects.create(
            external_id=external_id,
            raw_data=raw_data,
            nombre=nombre,
            fecha_publicacion=fecha_publicacion,
            fecha_apertura=fecha_apertura,
            cod_country=cod_country,
            origen=origen,
            isocode=Moneda.objects.get(isocode=isocode),
            id_licitante=Licitante.objects.get(id_licitante=id_licitante),
            id_estado_licitacion=EstadoLicitacion.objects.get(id_estado_licitacion=id_estado_licitacion),
            pushed=pushed)

        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


# licitante
@api_view(['GET'])
def get_licitante(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            licitante: list = [Licitante.objects.get(id_licitante=arg)]
        except ObjectDoesNotExist:
            licitante = []
    else:
        licitante: list = Licitante.objects.all()
    serializer: LicitanteSerializer = LicitanteSerializer(licitante, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_licitante(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    siglas: str = body.get("siglas", None)
    raw_data: str = body.get("raw_data", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        Licitante.objects.create(
            nombre=nombre,
            siglas=siglas,
            raw_data=raw_data)

        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)
