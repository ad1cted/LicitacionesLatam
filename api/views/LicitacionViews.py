import json

from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Moneda, Licitacion, Pais, Organismo, Ejecutivo
from kernel.serializers import LicitacionSerializer


@api_view(['GET'])
def get_licitacion(request: WSGIRequest, arg: str = None):
    if arg:
        licitacion: list = [Licitacion.objects.get(id=arg)]
    else:
        licitacion: list = Licitacion.objects.all()
    serializer: LicitacionSerializer = LicitacionSerializer(licitacion, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_licitacion(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)

    external_id: int = body.get("external_id", None)
    raw_data: str = body.get("raw_data", None)
    titulo: str = body.get("titulo", None)
    fecha_licitacion: str = body.get("fecha_licitacion", None)
    importe_contrato: str = body.get("importe_contrato", None)
    try:
        isocode_moneda: str = body.get("isocode_moneda", None)
        moneda = Moneda.objects.get(isocode=isocode_moneda)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con moneda"})
    try:
        isocode_pais: str = body.get("isocode_pais", None)
        pais = Pais.objects.get(isocode=isocode_pais)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con pais"})
    try:
        id_ejecutivo: str = body.get("id_Ejecutivo", None)
        ejecutivo = Ejecutivo.objects.get(id=id_ejecutivo)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con ejecutivo"})
    try:
        id_organismo: str = body.get("id_Organismo", None)
        organismo = Organismo.objects.get(id=id_organismo)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con organismo"})

    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if titulo:
        Licitacion.objects.create(
            titulo=titulo,
            fecha_licitacion=fecha_licitacion,
            importe_contrato=importe_contrato,
            id_Moneda=moneda,
            raw_data=raw_data,
            external_id=external_id,
            id_Pais=pais,
            id_Organismo=organismo,
            id_Ejecutivo=ejecutivo)

        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)
