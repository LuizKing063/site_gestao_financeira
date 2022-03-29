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
    list_display = ('email', 'username', 'is_staff', 'is_active')
    list_filter = ('email', 'username', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')
