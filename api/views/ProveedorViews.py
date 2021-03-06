import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Proveedor, \
    Localidad, Pais
from kernel.serializers import ProveedorSerializer


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
    raw_data: str = body.get("raw_data", None)
    dni: str = body.get("dni", None)
    isocode: str = body.get("isocode", None)
    try:
        isocode = Localidad.objects.get(isocode=isocode)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "isocode de localidad incorrecto"})
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre and dni:
        Proveedor.objects.create(
            nombre=nombre,
            razon_social=razon_social,
            descripcion=descripcion,
            raw_data=raw_data,
            dni=dni,
            id_localidad=isocode,
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_proveedor(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Proveedor.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"Proveedor id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el Proveedor, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})


@api_view(['POST'])
def update_proveedor(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    id: int = body.get("id", None)
    proveedor = Proveedor.objects.get(id=id)
    nombre: str = body.get("nombre", None)
    razon_social: str = body.get("razon_social", None)
    descripcion: str = body.get("descripcion", None)
    raw_data: int = body.get("raw_data", None)
    dni: str = body.get("dni", None)
    isocode: str = body.get("isocode", None)
    fecha_inicio_actividades: str = body.get("fecha_inicio_actividades", None)
    proveedor.nombre = nombre
    proveedor.razon_social = razon_social
    proveedor.descripcion = descripcion
    proveedor.raw_data = raw_data
    proveedor.dni = dni
    proveedor.fecha_inicio_actividades = fecha_inicio_actividades
    proveedor.isocode = Pais.objects.get(isocode=isocode)
    proveedor.save()
    return Response(status=status.HTTP_200_OK)
