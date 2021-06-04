import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import RolEjecutivo, Rol, Ejecutivo
from kernel.serializers import RolEjecutivoSerializer


@api_view(['GET'])
def get_rolEjecutivo(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            rolEjecutivo: list = [RolEjecutivo.objects.get(id=arg)]
        except ObjectDoesNotExist:
            rolEjecutivo = []
    else:
        rolEjecutivo: list = RolEjecutivo.objects.all()
    serializer: RolEjecutivoSerializer = RolEjecutivoSerializer(rolEjecutivo, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_rolEjecutivo(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    id_Rol: bool = body.get("id_Rol", None)
    try:
        rol = Rol.objects.get(id=id_Rol)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el rol que indicas"})
    id_Ejecutivo: dict = body.get("id_Ejecutivo", None)
    try:
        ejecutivo = Ejecutivo.objects.get(id=id_Ejecutivo)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el ejecutivo que indicas"})

    if id_Rol and id_Ejecutivo:
        try:
            RolEjecutivo.objects.create(
                id_Rol=rol,
                id_Ejecutivo=ejecutivo,

            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "error con rol, es proable que ya exista"})
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=sended_status)


@api_view(['GET'])
def delete_rolEjecutivo(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            RolEjecutivo.objects.get(id=arg)
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"ProveeRolEjecutivodor id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el RolEjecutivo, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
