from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .serializers import (PaymentSerializer,
                          )
from apps.payments.models import Payment
from apps.accounts.models import User
from apps.barbers.models import Barber


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_payment(request):
    try:
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            reserve = serializer.validated_data.get('reserve')
            check = Payment.objects.filter(reserve=reserve, status='p')
            if check:
                return Response(
                    data={
                        'msg': "Paid already"
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE
                )

            serializer.save()

            return Response(
                data={
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    'msg': serializer.errors
                },
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
def user_payments(request):
    try:
        user = User.objects.get(username=request.user)
        list_payments = Payment.objects.filter(reserve__user=user)
        serializer = PaymentSerializer(list_payments, many=True)

        return Response(
            data={
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            data={
                'data': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def barber_payments(request):
    try:
        print(request.user)
        barber = Barber.objects.get(barber=request.user)
        list_payments = Payment.objects.filter(reserve__barber=barber)
        serializer = PaymentSerializer(list_payments, many=True)

        return Response(
            data={
                'data': serializer.data
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
                'data': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )