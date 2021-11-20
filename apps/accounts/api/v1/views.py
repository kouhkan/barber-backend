from django.db import IntegrityError

from rest_framework.views import Response
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.tokens import RefreshToken

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.accounts.models import User
from utils.drf_params import jwt_key
from utils.redis_utils import (add_user_to_redis,
                               get_user_from_redis,
                               delete_user_from_redis)
from .serializers import (UserRegisterSerializer,
                          UserActivationSerializer,
                          UserLoginSerializer,
                          UserResendSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth_register(request):
    try:
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            token = add_user_to_redis(new_user, 'register')
            print(token)
            return Response(
                data={'data': serializer.validated_data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    except ValueError as v:
        return Response(
            data={
                'data': str(v)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    except IntegrityError as i:
        return Response(
            data={
                'data': str(i)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['PATCH'])
@permission_classes([permissions.AllowAny])
def auth_activation(request):
    try:
        serializer = UserActivationSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data.get('token')
            username = serializer.validated_data.get('username')

            user = User.objects.get(username=username)

            # if user.is_active:
            #     get_user = get_user_from_redis(user, 'resend')
            #     if not get_user:
            #         return Response(
            #             data={'msg': "Code does not exist"},
            #             status=status.HTTP_404_NOT_FOUND
            #         )
            #     if delete_user_from_redis(user, 'resend'):
            #         refresh_token = RefreshToken.for_user(user)
            #         access_token = refresh_token.access_token
            #         return Response(
            #             data={
            #                 'token': {
            #                     'access': str(access_token),
            #                     'refresh': str(refresh_token)
            #                 }
            #             },
            #             status=status.HTTP_200_OK
            #         )

            get_user = get_user_from_redis(user, 'register') or \
                       get_user_from_redis(user, 'resend')

            if not get_user:
                return Response(
                    data={'msg': "Code expired or wrong"},
                    status=status.HTTP_404_NOT_FOUND
                )
            if token != get_user.decode('UTF-8'):
                return Response(
                    data={'msg': "Code does not matched"},
                    status=status.HTTP_404_NOT_FOUND
                )

            if not user.is_active:
                user.is_active = True
                user.save()

            if delete_user_from_redis(user, 'register') or \
                    delete_user_from_redis(user, 'resend'):
                refresh_token = RefreshToken.for_user(user)
                access_token = refresh_token.access_token
                return Response(
                    data={
                        'token': {
                            'access': str(access_token),
                            'refresh': str(refresh_token)
                        }
                    },
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except ValueError as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_400_BAD_REQUEST
        )
    except User.DoesNotExist as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth_login(request):
    try:
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')

            user = User.objects.get(username=username)

            if not user.is_active:
                token = add_user_to_redis(user, 'register')
                print(token)
                return Response(
                    data={'msg': "User is not active"},
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )

            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            return Response(
                data={
                    'token': {
                        'access': str(access_token),
                        'refresh': str(refresh_token)
                    }
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except ValueError as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_400_BAD_REQUEST
        )
    except User.DoesNotExist as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_404_NOT_FOUND
        )


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def auth_resend(request):
    try:
        serializer = UserResendSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            user = User.objects.get(username=username)

            token = add_user_to_redis(user, 'resend')
            print(token)

            return Response(
                data={
                    'msg': "Code resend"
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except ValueError as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_400_BAD_REQUEST
        )
    except User.DoesNotExist as v:
        return Response(
            data={'msg': str(v)},
            status=status.HTTP_404_NOT_FOUND
        )
