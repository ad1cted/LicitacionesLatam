import json

from django.core.handlers.wsgi import WSGIRequest
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Moneda
from kernel.serializers import MonedaSerializer


@api_view(['GET'])
def get_moneda(request: WSGIRequest, isocode: str = None) -> Response:
    if isocode:
        monedas: list = [Moneda.objects.get(isocode=isocode)]
    else:
        monedas: list = Moneda.objects.all()
    serializer: MonedaSerializer = MonedaSerializer(monedas, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_moneda(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    isocode: str = body.get("isocode", None)
    if len(isocode) != 3:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "isocode no cumple formato"})
    nombre: str = body.get("nombre", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if isocode and nombre:
        try:
            Moneda.objects.create(isocode=isocode, nombre=nombre)
            sended_status: int = status.HTTP_201_CREATED
        except IntegrityError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "la moneda ya existe"})
    return Response(status=sended_status)

@api_view(['GET'])
def delete_moneda(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Moneda.objects.get(id=arg)
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"Moneda id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el Moneda, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
