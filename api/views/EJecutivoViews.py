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
def get_ejecutivo(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            ejecutivo: list = [Ejecutivo.objects.get(isocode=arg)]
        except ObjectDoesNotExist:
            ejecutivo = []
    else:
        ejecutivo: list = Ejecutivo.objects.all()
    serializer: EjecutivoSerializer = EjecutivoSerializer(ejecutivo, many=True)
    return Response(serializer.data)
