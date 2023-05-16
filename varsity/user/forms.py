from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    bio = forms.CharField(max_length=500, required=False)
    avatar = forms.ImageField(max_length=1224, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
