from ..models.objects import RegistroHeader, RegistroDetalhe
from .serializers import RegistroHeaderSerializer, RegistroDetalheSerializer
from rest_framework import viewsets


class RegistroHeaderViewSet(viewsets.ModelViewSet):
    queryset = RegistroHeader.objects.all()
    serializer_class = RegistroHeaderSerializer


class RegistroDetalheViewSet(viewsets.ModelViewSet):
    queryset = RegistroDetalhe.objects.all()
    serializer_class = RegistroDetalheSerializer
