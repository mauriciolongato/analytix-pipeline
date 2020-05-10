from rest_framework import serializers
from .models.objects import RegistroHeader, RegistroDetalhe


class RegistroHeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroHeader
        fields = '__all__'


class RegistroDetalheSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroDetalhe
        fields = '__all__'


class RegistroDetalheSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroDetalhe
        fields = '__all__'
