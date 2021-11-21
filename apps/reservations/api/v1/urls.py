from django.urls import path

from . import views


app_name = 'reservations'

urlpatterns = [
    path('time/', views.reserve_time, name='reserve_time'),
]