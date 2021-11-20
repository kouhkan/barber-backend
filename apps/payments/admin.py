from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('reserve', 'code', 'authority', 'created', 'status')
    list_filter = ('status', )
    list_editable = ('status', )
    search_fields = ('code', 'authority')
    raw_id_fields = ('reserve', )
    list_per_page = 50