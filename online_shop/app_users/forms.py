from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from phonenumber_field.formfields import PhoneNumberField

from .models import User


class LoginForm(AuthenticationForm):
    """Форма для логина пользователя"""

    username = forms.CharField(label='Введите email', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'test@gmail.com'}))
    password = forms.CharField(label='Введите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class RegistrationForm(UserCreationForm):
    """Форма для регистрации пользователя"""

    first_name = forms.CharField(label='Имя*', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(label='Фамилия*', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Иванов'}))
    patronymic = forms.CharField(label='Отчество',  required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Иванович'}))
    email = forms.CharField(label='Эл. почта*', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'test@gmail.com'}))
    phone_number = PhoneNumberField(label='Номер телефона*', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '+78005553535 '}))
    phone_number.error_messages['invalid'] = 'Неверный формат (+78005553535)'
    password1 = forms.CharField(label='Пароль*', widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Минимум 8 символов, в т.ч цифры'}))
    password2 = forms.CharField(label='Подтвердите пароль*', widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'email', 'phone_number', 'password1', 'password2')
