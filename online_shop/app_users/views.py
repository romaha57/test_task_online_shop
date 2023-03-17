from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from app_products.models import Basket, Order
from .forms import LoginForm, RegistrationForm
from .models import User


class UserLoginView(LoginView):
    """Аутентификация пользователя"""

    form_class = LoginForm
    template_name = 'app_users/login.html'


class UserLogoutView(LogoutView):
    """Выход пользователя"""

    next_page = reverse_lazy('app_products:home')


class UserRegistrationView(CreateView):
    """Регистрация пользователя"""

    model = User
    form_class = RegistrationForm
    template_name = 'app_users/signup.html'
    success_url = reverse_lazy('app_users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['messages'] = messages.info(self.request, message='Вы успешно зарегистрировались')

        return context


class UserProfileView(LoginRequiredMixin, ListView):
    """Личный кабинет пользователя"""

    template_name = 'app_users/user_profile.html'
    context_object_name = 'baskets'

    def get_queryset(self):
        """Фильтруем товары только для конкретного пользователя"""

        return Basket.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        """Получаем все заказы исходя из их статуса"""

        context = super().get_context_data(**kwargs)
        context['created_orders'] = Order.objects.filter(owner=self.request.user).filter(status=1)
        context['confirmed_orders'] = Order.objects.filter(owner=self.request.user).filter(status=2)
        context['rejected_orders'] = Order.objects.filter(owner=self.request.user).filter(status=3)

        return context