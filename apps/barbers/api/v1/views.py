from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination

from apps.barbers.models import Barber, Service
from .serializers import (BarbersSerializer,
                          BarberNameSerializer,
                          ServiceSerializer)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def barbers_list(request):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 25
        barbers = Barber.objects.filter(status=True)
        barbers_page = paginator.paginate_queryset(barbers, request)
        serializers = BarbersSerializer(barbers_page, many=True)
        return Response(
            data={
                'data': paginator.get_paginated_response(serializers.data).data
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            data={
                'msg': str(e)
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def barbers_search(request):
    try:
        serializer = BarberNameSerializer(data=request.data)
        if serializer.is_valid():
            shop_name = serializer.validated_data.get('shop_name')
            barber_list = Barber.objects.filter(shop_name__icontains=shop_name)
            barbers_serializer = BarbersSerializer(barber_list, many=True)

            return Response(
                data={
                    'data': barbers_serializer.data
                },
                status=status.HTTP_200_OK
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
@permission_classes([permissions.AllowAny])
def get_barber(request, barber_id):
    try:
        barber = Barber.objects.get(id=barber_id)
        barber_services = Service.objects.filter(barber=barber)
        barbers_serializer = BarbersSerializer(barber)
        barber_services_serializer = ServiceSerializer(barber_services, many=True)

        return Response(
            data={
                'data': {
                    'barber': barbers_serializer.data,
                    'services': barber_services_serializer.data
                }
            },
            status=status.HTTP_200_OK
        )
    except Barber.DoesNotExist:
        return Response(
            data={
                'msg': 'Barber does not exist'
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


