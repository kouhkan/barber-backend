from django.urls import path
from . import views


app_name = 'barbers'


urlpatterns = [
    path('list/', views.barbers_list, name='barbers_list'),
    path('search/', views.barbers_search, name='barbers_search'),
    path('<int:barber_id>/', views.get_barber, name='get_barber'),
]