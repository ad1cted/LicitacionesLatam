import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Proveedor, \
    ProveedorLicitacion, Licitacion, EstadoProvedorLicitacion
from kernel.serializers import ProveedorLicitacionSerializer


# proveedor
@api_view(['GET'])
def get_proveedorLicitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            proveedorLicitacion: list = [ProveedorLicitacion.objects.get(id=arg)]
        except ObjectDoesNotExist:
            proveedorLicitacion = []
    else:
        proveedorLicitacion: list = ProveedorLicitacion.objects.all()
    serializer: ProveedorLicitacionSerializer = ProveedorLicitacionSerializer(proveedorLicitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_proveedorLicitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    raw_data: str = body.get("raw_data", None)
    try:
        id_Licitacion: str = body.get("id_Licitacion", None)
        licitacion = Licitacion.objects.get(id=id_Licitacion)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "licitacion incorrecto"})
    try:
        id_EstadoProvedorLicitacion: str = body.get("id_EstadoProvedorLicitacion", None)
        estadoProvedorLicitacion = EstadoProvedorLicitacion.objects.get(id=id_EstadoProvedorLicitacion)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "estadoProvedorLicitacionincorrecto"})
    try:
        id_Proveedor: str = body.get("id_Proveedor", None)
        proveedor = Proveedor.objects.get(id=id_Proveedor)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "isocode incorrecto"})
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if raw_data:
        ProveedorLicitacion.objects.create(
            raw_data=raw_data,
            id_Licitacion=licitacion,
            id_EstadoProvedorLicitacion=estadoProvedorLicitacion,
            id_Proveedor=proveedor

        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)
