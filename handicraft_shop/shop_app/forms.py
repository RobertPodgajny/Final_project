from django import forms
from django.forms import ModelForm

from shop_app.models import User


class LoginForm(forms.Form):
    nick = forms.CharField(label='Twój nick', max_length=64)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'nick': 'Twój nick',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Email',
            'password': 'Hasło',
            'password2': 'Powtórz hasło',
            'address': 'Podaj adres do wysyłki'
        }
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
