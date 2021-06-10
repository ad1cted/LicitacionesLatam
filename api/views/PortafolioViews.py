import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import EstatusProveedor, Proveedor, Portafolio, Ejecutivo
from kernel.serializers import PortafolioSerializer


@api_view(['GET'])
def get_portafolio(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            portafolio: list = [Portafolio.objects.get(id=arg)]
        except ObjectDoesNotExist:
            portafolio = []
    else:
        portafolio: list = Portafolio.objects.all()
    serializer: PortafolioSerializer = PortafolioSerializer(portafolio, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_portafolio(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)

    id_Ejecutivo: dict = body.get("id_Ejecutivo", None)

    try:
        ejecutivo = Ejecutivo.objects.get(id=id_Ejecutivo)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el ejecutivo que indicas"})

    id_Proveedor: dict = body.get("id_Proveedor", None)
    try:
        proveedor = Proveedor.objects.get(id=id_Proveedor)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el proveedor que indicas"})

    try:
        Portafolio.objects.create(
            id_Ejecutivo=ejecutivo,
            id_Proveedor=proveedor
        )
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "error con Portafolio, es proable que ya exista"})
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def delete_portafolio(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Portafolio.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"Portafolio id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el Portafolio, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})


@api_view(['POST'])
def update_portafolio(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    portafolio: Portafolio = Portafolio.objects.get(id=body.get("id", None))
    portafolio.id_Proveedor = Proveedor.objects.get(id=body.get("id_Proveedor", None))
    portafolio.id_Ejecutivo = Ejecutivo.objects.get(id=body.get("id_Ejecutivo", None))
    portafolio.save()
    return Response(status=status.HTTP_200_OK)
