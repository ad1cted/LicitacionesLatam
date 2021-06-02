import json

from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Localidad, Pais
from kernel.serializers import LocalidadSerializer


@api_view(['GET'])
def get_localidad(request: WSGIRequest, isocode: str = None) -> Response:
    if isocode:
        monedas: list = [Localidad.objects.get(isocode=isocode)]
    else:
        monedas: list = Localidad.objects.all()
    serializer: LocalidadSerializer = LocalidadSerializer(monedas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_localidad(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    codigo_area: int = body.get("codigo_area", None)
    nombre: str = body.get("nombre", None)
    isocode_id: str = body.get("isocode", None)
    try:
        pais = Pais.objects.get(isocode=isocode_id)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con isocode"})

    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if codigo_area and nombre:
        try:
            Localidad.objects.create(codigo_area=codigo_area, nombre=nombre, isocode_id=pais.isocode)
            sended_status: int = status.HTTP_201_CREATED
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "la localidad ya existe"})
    return Response(status=sended_status)
