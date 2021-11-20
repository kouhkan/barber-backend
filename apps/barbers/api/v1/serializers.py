from rest_framework import serializers

from apps.barbers.models import Barber, Service


class BarbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        exclude = ('created', 'updated')


class BarberNameSerializer(serializers.Serializer):
    shop_name = serializers.CharField(min_length=3, max_length=128)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude = ('created', 'updated')


