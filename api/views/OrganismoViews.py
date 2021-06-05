import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Organismo, Localidad
from kernel.serializers import OrganismoSerializer


@api_view(['GET'])
def get_organismo(request: WSGIRequest, arg: int = None) -> Response:
    if arg:
        try:
            organismo: list = [Organismo.objects.get(id=arg)]
        except ObjectDoesNotExist:
            organismo = []
    else:
        organismo: list = Organismo.objects.all()
    serializer: OrganismoSerializer = OrganismoSerializer(organismo, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_organismo(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: bool = body.get("nombre", None)
    descripcion: str = body.get("descripcion", None)
    dni: str = body.get("dni", None)
    id_Localidad: int = body.get("id_Localidad", None)

    sended_status = status.HTTP_206_PARTIAL_CONTENT
    try:
        localidad = Localidad.objects.get(id=id_Localidad)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "error con Localidad indicada"})

    if nombre:
        Organismo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            dni=dni,
            id_Localidad=localidad
        )
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)

@api_view(['GET'])
def delete_organismo(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Organismo.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"Organismo id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el Organismo, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
