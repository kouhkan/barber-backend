"""A URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps urls
    path('api/v1/', include([
        path(
            'auth/',
            include('apps.accounts.api.v1.urls'),
            name='auth'
        ),
        path(
            'barbers/',
            include('apps.barbers.api.v1.urls'),
            name='barbers'
        ),
        path(
            'reserves/',
            include('apps.reservations.api.v1.urls'),
            name='reservations'
        )
    ]))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Barber Reservation API",
            default_version='v1',
            description="A document for Barber ",
            contact=openapi.Contact(email="amirkouhkan1@gmail.com"),
            license=openapi.License(name="CopyRight"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns += [
        # SWAGGER
        path('swagger/json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/ui/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('swagger/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    ]
