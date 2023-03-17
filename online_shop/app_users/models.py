from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель пользователя"""

    username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='email')
    patronymic = models.CharField(max_length=100, verbose_name='отчество', blank=True)
    phone_number = PhoneNumberField(verbose_name='номером телефона', unique=True)
    is_admin = models.BooleanField(default=False, verbose_name='админ')

    # устанавливаем аутентификацию по email
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.email} // {self.phone_number}'