from django.urls import path
from . import views


app_name = 'auth'


urlpatterns = [
    path('register/', views.auth_register, name='auth_register'),
    path('activation/', views.auth_activation, name='auth_activation'),
    path('login/', views.auth_login, name='auth_login'),
    path('resend/', views.auth_resend, name='auth_resend'),
]
