import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import TipoContacto, Proveedor, \
    Contacto
from kernel.serializers import ContactoSerializer


@api_view(['GET'])
def get_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            contacto: list = [Contacto.objects.get(id=arg)]
        except ObjectDoesNotExist:
            contacto = []
    else:
        contacto: list = Contacto.objects.all()
    serializer: ContactoSerializer = ContactoSerializer(contacto, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_contacto(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    activo: bool = body.get("activo", None)
    valor: str = body.get("valor", None)
    id_proveedor: int = body.get("id_proveedor", None)
    id_tipo_contacto: int = body.get("id_tipo_contacto", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    try:
        proveedor = Proveedor.objects.get(id=id_proveedor)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con Proveedor indicado"})
    try:
        tipo_contacto = TipoContacto.objects.get(id=id_tipo_contacto)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con Tipo_contacto indicado"})
    if valor:
        Contacto.objects.create(
            activo=activo,
            valor=valor,
            id_Proveedor=proveedor,
            id_TipoContacto=tipo_contacto
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Contacto.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK, data={"message": f"contacto id={arg} correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el contacto, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
