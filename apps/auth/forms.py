import re
from django import forms
from django.conf import settings
from apps.users.service import UsersService
from smartedu.common.constants import Regex


class LoginForm(forms.Form):
    _usersService = UsersService()
    
    email = forms.EmailField(
        label='Електронна адреса',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
        error_messages={'required': 'Будь ласка, введіть електронну адресу'}
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль'}),
        error_messages={'required': 'Будь ласка, введіть пароль'}
    )
    remember = forms.BooleanField(
        label='Запам’ятати мене',
        required=False,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(Regex.EMAIL, email):
            raise forms.ValidationError('Невірна електронна адреса')

        if not self._usersService.exists(email):
            raise forms.ValidationError('Користувач з такою електронною адресою не зареєстрований на сайті')

        return email
    
    def clean_remember(self):
        remember = self.cleaned_data.get('remember')
        if remember not in [True, False, None]:
            raise forms.ValidationError('Некоректне значення поля "Запам’ятати мене"')
        return remember

class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Електронна адреса',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'example@gmail.com'}),
        error_messages={'required': 'Будь ласка, введіть електронну адресу'}
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Введіть пароль'}),
        error_messages={'required': 'Будь ласка, введіть пароль'}
    )
    first_name = forms.CharField(
        label='Ім’я',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ім’я'}),
        error_messages={'required': 'Будь ласка, введіть ім’я'}
    )
    second_name = forms.CharField(
        label='Прізвище',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Прізвище'}),
        error_messages={'required': 'Будь ласка, введіть прізвище'}
    )
    remember = forms.BooleanField(
        label='Запам’ятати мене',
        required=False,
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        domain = email.split('@')[1]

        if not re.match(Regex.EMAIL, email):
            raise forms.ValidationError('Невірна електронна адреса')

        if self._usersService.exists(email):
            raise forms.ValidationError('Користувач з такою електронною адресою вже зареєстрований на сайті')

        if not settings.DEBUG and domain != "chnu.edu.ua":
            raise forms.ValidationError('Ця електронна адреса не з Чернівецького університету. Наші всі на @chnu.edu.ua 😉')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Пароль має містити щонайменше 8 символів')
        return password

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not re.match(Regex.USERNAME_LENGTH, first_name):
            raise forms.ValidationError('Ім’я повинно містити лише літери та мати від 2 до 30 символів')
        return first_name

    def clean_second_name(self):
        second_name = self.cleaned_data.get('second_name')
        if not re.match(Regex.USERNAME_LENGTH, second_name):
            raise forms.ValidationError('Прізвище повинно містити лише літери та мати від 2 до 30 символів')
        return second_name

    def clean_remember(self):
        remember = self.cleaned_data.get('remember')
        if remember not in [True, False, None]:
            raise forms.ValidationError('Некоректне значення поля "Запам’ятати мене"')
        return remember