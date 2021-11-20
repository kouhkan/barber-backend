from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserProfile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'full_name', 'is_active')
    list_filter = ('is_active', )
    list_per_page = 25
    list_editable = ('is_active', )
    search_fields = ('username', 'full_name')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'date_joined',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'status')
    list_filter = ('status', 'created')
    list_editable = ('status',)
    list_per_page = 25
    search_fields = ('user', )

