from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.reservations.models import Reserve

from .serializers import ReserveSerializer


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

