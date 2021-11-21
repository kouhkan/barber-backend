from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.reservations.models import Reserve
from apps.barbers.models import Barber
from apps.accounts.models import User

from .serializers import (ReserveSerializer, )


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def reserve_time(request):
    print(request.user)
    try:
        serializer = ReserveSerializer(data=request.data)
        if serializer.is_valid():
            barber = serializer.validated_data.get('barber')
            date = serializer.validated_data.get('date')
            time = serializer.validated_data.get('time')

            check = Reserve.objects.filter(barber=barber, date=date,
                                           time=time, status='r')

            if check:
                return Response(
                    data={
                        'msg': 'Time reserved'
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )

            serializer.save(user=request.user)

            return Response(
                data={
                    'data': serializer.data,
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        return Response(
            data={
                'msg': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def barber_reservations_list(request):
    try:
        barber = Barber.objects.get(barber=request.user)
        barber_reservations = Reserve.objects.filter(barber=barber)
        reservations_list = ReserveSerializer(barber_reservations, many=True)

        return Response(
            data={
                'data': reservations_list.data
            },
            status=status.HTTP_200_OK
        )
    except Barber.DoesNotExist:
        return Response(
            data={
                'msg': "Barber does not exist"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            data={
                'msg': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_reservations_list(request):
    try:
        user = User.objects.get(username=request.user)
        user_reservations = Reserve.objects.filter(user=user)
        reservations_list = ReserveSerializer(user_reservations, many=True)

        return Response(
            data={
                'data': reservations_list.data
            },
            status=status.HTTP_200_OK
        )
    except Barber.DoesNotExist:
        return Response(
            data={
                'msg': "User does not exist"
            },
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            data={
                'msg': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )
