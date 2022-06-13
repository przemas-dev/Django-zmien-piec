from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Nazwa użytkownika', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Imię',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko',max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Hasło',max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Powtórz hasło',max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "password1", "password2")
