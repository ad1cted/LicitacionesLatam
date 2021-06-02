import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Moneda, Licitacion, Pais
from kernel.serializers import LicitacionSerializer


def get_licitacion(request: WSGIRequest, arg: str = None, isocode: str = None):
    if isocode:
        try:
            print(Pais.objects.all().count())
            pais = Pais.objects.filter(nombre__exact='Mexico')
            print(pais)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    if arg:

        try:
            licitacion: list = [Licitacion.objects.get(id=arg)]
        except ObjectDoesNotExist:
            licitacion = []
    else:
        licitacion: list = Licitacion.objects.all()
    serializer: LicitacionSerializer = LicitacionSerializer(licitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    external_id: str = body.get("external_id", None)
    raw_data: str = body.get("raw_data", None)
    nombre: str = body.get("nombre", None)
    fecha_publicacion: str = body.get("fecha_publicacion", None)
    fecha_apertura: str = body.get("fecha_apertura", None)
    cod_country: str = body.get("cod_country", None)
    origen: str = body.get("origen", None)
    isocode: str = body.get("isocode", None)
    id_licitante: str = body.get("id_licitante", None)
    id_estado_licitacion: str = body.get("id_estado_licitacion", None)
    pushed: bool = body.get("pushed", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre and isocode and id_estado_licitacion:
        Licitacion.objects.create(
            external_id=external_id,
            raw_data=raw_data,
            nombre=nombre,
            fecha_publicacion=fecha_publicacion,
            fecha_apertura=fecha_apertura,
            cod_country=cod_country,
            origen=origen,
            isocode=Moneda.objects.get(isocode=isocode),
            pushed=pushed)

        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)
