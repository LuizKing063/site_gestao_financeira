from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.user_model import User
from .forms.user_form import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(UserAdmin):
    """Custom user admin."""

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')
