from rest_framework import serializers
from apps.reservations.models import Reserve
from apps.accounts.models import User


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        exclude = ('created', 'updated')
        extra_kwargs = {'user': {'required': False}}


