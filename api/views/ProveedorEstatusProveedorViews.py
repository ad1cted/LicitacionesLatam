import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from kernel.models import EstatusProveedor, ProveedorEstatusProveedor, Proveedor
from kernel.serializers import ProveedorEstatusProveedorSerializer


@api_view(['GET'])
def get_proveedorEstatus_proveedor(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            proveedorEstatus_proveedor: list = [ProveedorEstatusProveedor.objects.get(id=arg)]
        except ObjectDoesNotExist:
            proveedorEstatus_proveedor = []
    else:
        proveedorEstatus_proveedor: list = ProveedorEstatusProveedor.objects.all()
    serializer: ProveedorEstatusProveedorSerializer = ProveedorEstatusProveedorSerializer(proveedorEstatus_proveedor,
                                                                                          many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_proveedorEstatus_proveedor(request: WSGIRequest) -> Response:
    body: dict = json.loads(request.body)
    raw_data: str = body.get("raw_data", None)
    id_EstatusProveedor: bool = body.get("id_EstatusProveedor", None)
    try:
        estatusProveedor = EstatusProveedor.objects.get(id=id_EstatusProveedor)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el estatusProveedor que indicas"})
    id_Proveedor: dict = body.get("id_Proveedor", None)
    try:
        proveedor = Proveedor.objects.get(id=id_Proveedor)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": "no existe el proveedor que indicas"})

    if raw_data:
        try:
            ProveedorEstatusProveedor.objects.create(
                id_Proveedor=proveedor,
                id_EstatusProveedor=estatusProveedor,
                raw_data=raw_data
            )
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"error": "error con ProveedorEstatusProveedor, es proable que ya exista"})
        sended_status: int = status.HTTP_201_CREATED
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def delete_proveedorEstatus_proveedor(request: WSGIRequest, arg: str = None) -> Response:
    if arg:
        try:
            ProveedorEstatusProveedor.objects.get(id=arg).delete()
            return Response(status=status.HTTP_200_OK,
                            data={"message": f"proveedorEstatus_proveedor id={arg} borrado correctamente"})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={"error": "imposible borrar el proveedorEstatus_proveedor, es posible que ni exista"})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "no has indicado el id a borrar"})
