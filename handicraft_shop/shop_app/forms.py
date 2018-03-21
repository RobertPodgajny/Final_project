from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from shop_app.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Twój login', max_length=64)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class RegistrationForm(ModelForm):
    username = forms.CharField(required=True, label="Twój login")
    new_password = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput())
    address = forms.CharField(label='Adres', widget=forms.Textarea, help_text="Podaj adres do wysyłki")

    def clean(self):
        new_password = self.cleaned_data['new_password']
        new_password2 = self.cleaned_data['new_password2']

        if new_password != new_password2:
            raise ValidationError("Hasła muszą być takie same!")

    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Twój login',
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Email',
            'password': 'Hasło',
            'password2': 'Powtórz hasło',
            'address': 'Podaj adres do wysyłki'
        }

