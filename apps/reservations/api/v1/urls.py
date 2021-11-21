from django.urls import path

from . import views


app_name = 'reservations'

urlpatterns = [
    path('time/',
         views.reserve_time,
         name='reserve_time'),
    path('barber_list/',
         views.barber_reservations_list,
         name='barber_reservations_list'),
    path('user_list/',
         views.user_reservations_list,
         name='user_reservations_list'),
]
