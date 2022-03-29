from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ..models.user_model import User


class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user."""

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    """Form for editing an existing user."""

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
