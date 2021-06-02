import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Pais
from kernel.serializers import PaisSerializer


@api_view(['POST'])
def create_pais(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    isocode: str = body.get("isocode", None).upper()
    if len(isocode) != 3:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "el isocode no cumple el formato"})
    nombre: str = body.get("nombre", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if isocode and nombre:
        try:
            Pais.objects.create(isocode=isocode, nombre=nombre)
            sended_status: int = status.HTTP_201_CREATED
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "el pais ya existe"})
    return Response(status=sended_status)


@api_view(['GET'])
def get_pais(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            pais: list = [Pais.objects.get(isocode=arg)]
        except ObjectDoesNotExist:
            pais = []
    else:
        pais: list = Pais.objects.all()
    serializer: PaisSerializer = PaisSerializer(pais, many=True)
    return Response(serializer.data)
