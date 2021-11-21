from django.urls import path

from . import views


app_name = 'payments'


urlpatterns = [
    path('create/',
         views.create_payment,
         name='create_payment'),
    path('user/',
         views.user_payments,
         name='user_payments'),
    path('barber/',
         views.barber_payments,
         name='barber_payments')
]
