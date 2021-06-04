import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import Rol
from kernel.serializers import RolSerializer


@api_view(['GET'])
def get_rol(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            rol: list = [Rol.objects.get(id_contacto=arg)]
        except ObjectDoesNotExist:
            rol = []
    else:
        rol: list = Rol.objects.all()
    serializer: RolSerializer = RolSerializer(rol, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_rol(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    nombre: bool = body.get("nombre", None)
    configuracion: dict = body.get("configuracion", None)
    sended_status = status.HTTP_206_PARTIAL_CONTENT

    if nombre and configuracion:
        try:
            Rol.objects.create(
                nombre=nombre,
                configuracion=configuracion,

            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "error con rol, es proable que ya exista"})
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_rol(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            Rol.objects.get(id=arg)
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"Rol id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el Rol, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
