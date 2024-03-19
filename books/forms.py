from django import forms
from django.forms import ModelForm

from .models import Good


class SampleModelForm(ModelForm):
    class Meta:
        model = Good
        fields='__all__'

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')