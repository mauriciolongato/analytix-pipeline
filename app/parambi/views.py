from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models.objects import RegistroHeader, RegistroDetalhe
from .serializers import RegistroHeaderSerializer, RegistroDetalheSerializer


@api_view(['GET', 'POST'])
def registroheader_list(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        usuarios = RegistroHeader.objects.all()
        serializer = RegistroHeaderSerializer(usuarios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistroHeaderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def registrodetalhe_list(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        pergunta_variavel = RegistroDetalhe.objects.all()
        serializer = RegistroDetalheSerializer(pergunta_variavel, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegistroDetalheSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

