import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import TipoLicitacion
from kernel.serializers import TipoLicitacionSerializer


# tipo contacto
@api_view(['GET'])
def get_tipo_licitacion(request: WSGIRequest, arg: int = None) -> Response:
    if arg:
        try:
            tipo_licitacion: list = [TipoLicitacion.objects.get(id=arg)]
        except ObjectDoesNotExist:
            tipo_licitacion = []
    else:
        tipo_licitacion: list = TipoLicitacion.objects.all()
    serializer: TipoLicitacionSerializer = TipoLicitacionSerializer(tipo_licitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_tipo_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        TipoLicitacion.objects.create(nombre=nombre, descripcion=descripcion)
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_tipo_licitacion(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            TipoLicitacion.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"TipoLicitacion id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el TipoLicitacion, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})


@api_view(['POST'])
def update_tipo_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    id: int = body.get("id", None)
    tipo_licitacion = TipoLicitacion.objects.get(id=id)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    tipo_licitacion.nombre = nombre
    tipo_licitacion.descripcion = descripcion
    tipo_licitacion.save()
    return Response(status=status.HTTP_200_OK)
