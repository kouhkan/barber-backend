from django.contrib import admin
from .models import Barber, Service


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ('barber', 'shop_name', 'created', 'status')
    list_editable = ('status', )
    list_filter = ('status', )
    search_fields = ('shop_name', 'barber', )
    raw_id_fields = ('barber', )
    list_per_page = 25


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('barber', 'service_name', 'amount', 'created', 'status')
    list_editable = ('amount', 'status')
    list_filter = ('status', )
    search_fields = ('barber', 'service_name')
    raw_id_fields = ('barber', )
    list_per_page = 50