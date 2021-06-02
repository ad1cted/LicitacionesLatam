import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Proveedor, \
    Localidad
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
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "isocode incorrecto"})
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
