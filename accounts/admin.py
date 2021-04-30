from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_active',)
    list_filter = ('email', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'full_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'full_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ['date_joined', 'last_login']
