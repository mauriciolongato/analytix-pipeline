from ..models.objects import Simulation, SimulationData
from .serializers import SimulationSerializer, SimulationDataSerializer
from rest_framework import viewsets


class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer


class SimulationDataViewSet(viewsets.ModelViewSet):
    queryset = SimulationData.objects.all()
    serializer_class = SimulationDataSerializer
