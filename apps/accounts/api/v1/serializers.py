from rest_framework import serializers
from apps.accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=11, max_length=11)


class UserActivationSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=4, min_length=4)
    username = serializers.CharField(max_length=11, min_length=11)


class UserResendSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=11, min_length=11)
