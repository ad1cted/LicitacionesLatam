import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import EstadoProvedorLicitacion
from kernel.serializers import EstadoProvedorLicitacionSerializer


# status_proveedor
@api_view(['GET'])
def get_estadoProveedor_licitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            estadoProvedorLicitacion: list = [EstadoProvedorLicitacion.objects.get(id_estado_proveedor=arg)]
        except ObjectDoesNotExist:
            estadoProvedorLicitacion = []
    else:
        estadoProvedorLicitacion: list = EstadoProvedorLicitacion.objects.all()
    serializer: EstadoProvedorLicitacionSerializer = EstadoProvedorLicitacionSerializer(estadoProvedorLicitacion,
                                                                                        many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_estadoProveedor_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        try:
            EstadoProvedorLicitacion.objects.create(
                nombre=nombre,
                descripcion=descripcion,
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "el estatus ya existe"})
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_estadoProveedor_licitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            EstadoProvedorLicitacion.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"EstadoProvedorLicitacion id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el EstadoProvedorLicitacion, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})


@api_view(['POST'])
def update_estadoProveedor_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    estadoProvedorLicitacion: EstadoProvedorLicitacion = EstadoProvedorLicitacion.objects.get(id=body.get("id", None))
    estadoProvedorLicitacion.nombre = body.get("nombre", None)
    estadoProvedorLicitacion.descripcion = body.get("descripcion", None)
    estadoProvedorLicitacion.save()
    return Response(status=status.HTTP_200_OK)
