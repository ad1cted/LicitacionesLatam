import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Ejecutivo
from kernel.serializers import EjecutivoSerializer


@api_view(['POST'])
def create_ejecutivo(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    id_externo: int = body.get("id_externo", None)
    username: str = body.get("username", None)
    activo: bool = body.get("activo", None)

    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if username and activo:
        try:
            Ejecutivo.objects.create(id_externo=id_externo, username=username, activo=activo)
            sended_status: int = status.HTTP_201_CREATED
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "el ejecutivo ya existe"})
    return Response(status=sended_status)


@api_view(['GET'])
def get_ejecutivo(request: WSGIRequest, arg: int = None) -> Response:
    if arg:
        try:
            ejecutivo: list = [Ejecutivo.objects.get(id=arg)]
        except ObjectDoesNotExist:
            ejecutivo = []
    else:
        ejecutivo: list = Ejecutivo.objects.all()
    serializer: EjecutivoSerializer = EjecutivoSerializer(ejecutivo, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def delete_ejecutivo(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Ejecutivo.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK, data={"message": f"ejecutivo id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el ejecutivo, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})


@api_view(['POST'])
def update_ejecutivo(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    id: int = body.get("id", None)
    ejecutivo = Ejecutivo.objects.get(id=id)
    id_externo: int = body.get("id_externo", None)
    username: str = body.get("username", None)
    activo: str = body.get("activo", None)
    ejecutivo.id_externo = id_externo
    ejecutivo.username = username
    ejecutivo.activo = activo
    ejecutivo.save()
    return Response(status=status.HTTP_200_OK)
