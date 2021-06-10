from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from utils.utils.views.MEX import views


@api_view(['GET'])
def deriva_datos_contacto(request: WSGIRequest, pais: str = None,empresa: str = None) -> Response:
    if pais == "MEX":
        return views.get_denue(empresa)
    elif pais == "CHI":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    elif pais == "PER":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"El pais {pais} NO ESTA SOPORTADO"})


@api_view(['GET'])
def deriva_datos_licitacion(request: WSGIRequest, pais: str = None, id_externo: int = None) -> Response:
    print(pais)
    if pais == "MEX":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    elif pais == "CHI":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    elif pais == "PER":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"El pais {pais} NO ESTA SOPORTADO"})


@api_view(['GET'])
def deriva_proveedor_sancionado(request: WSGIRequest, pais: str = None, dni: int = None) -> Response:
    if pais == "MEX":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    elif pais == "CHI":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    elif pais == "PER":
        return Response(status=status.HTTP_501_NOT_IMPLEMENTED,
                        data={"error": f"El pais {pais} NO ESTA SOPORTADO POR AHORA"})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": f"El pais {pais} NO ESTA SOPORTADO"})
