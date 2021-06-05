import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import TipoContacto
from kernel.serializers import TipoContactoSerializer


# tipo contacto
@api_view(['GET'])
def get_tipo_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            tipo_contacto: list = [TipoContacto.objects.get(id_tipo_contacto=arg)]
        except ObjectDoesNotExist:
            tipo_contacto = []
    else:
        tipo_contacto: list = TipoContacto.objects.all()
    serializer: TipoContactoSerializer = TipoContactoSerializer(tipo_contacto, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_tipo_contacto(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: str = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT
    if nombre:
        TipoContacto.objects.create(nombre=nombre,descripcion=descripcion)
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)

@api_view(['GET'])
def delete_tipo_contacto(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            TipoContacto.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"TipoContacto id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el TipoContacto, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
