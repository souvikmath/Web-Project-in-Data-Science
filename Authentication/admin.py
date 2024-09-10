from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    ordering = ['user_id']  # Adjust to your desired field for ordering
    list_display = ('user_id', 'email', 'is_staff', 'is_active')  # Adjust to your model fields
    search_fields = ('user_id', 'email')
    list_filter = ('is_staff', 'is_active')

    # Remove filter_horizontal if not using these fields
    filter_horizontal = []

    fieldsets = (
        (None, {'fields': ('user_id', 'email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
