from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from shop_app.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Twój login', max_length=64)
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)

    error_messages = {
        'invalid_login': "Podaj prawidłowy login i hasło",
        'inactive': "This account is inactive.",
    }


class RegistrationForm(ModelForm):
    username = forms.CharField(required=True, label="Twój login")
    new_password = forms.CharField(label='Podaj hasło', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Powtórz hasło', widget=forms.PasswordInput())
    address = forms.CharField(label='Adres', widget=forms.Textarea, help_text="Podaj adres do wysyłki")

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Użytkownik już istnieje w bazie")
        return self.cleaned_data['username']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Podany email już znajduje się w bazie")
        return self.cleaned_data['email']

    def clean(self):
        new_password = self.cleaned_data['new_password']
        new_password2 = self.cleaned_data['new_password2']

        if new_password != new_password2:
            raise ValidationError("Hasła muszą być takie same!")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Imię',
            'last_name': 'Nazwisko',
            'email': 'Email'
        }

