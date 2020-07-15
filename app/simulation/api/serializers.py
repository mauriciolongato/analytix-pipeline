from rest_framework import serializers
from ..models.objects import Simulation, SimulationData


class SimulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Simulation
        fields = '__all__'


class SimulationDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimulationData
        fields = '__all__'