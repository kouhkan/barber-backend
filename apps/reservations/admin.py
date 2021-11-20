from django.contrib import admin

from .models import Reserve


@admin.register(Reserve)
class ReserveAdmin(admin.ModelAdmin):
    list_display = ('user', 'barber', 'time', 'date', 'created', 'status')
    list_editable = ('status', 'date')
    list_filter = ('status', 'date')
    search_fields = ('user', 'barber')
    list_per_page = 25
    raw_id_fields = ('user', 'barber')

