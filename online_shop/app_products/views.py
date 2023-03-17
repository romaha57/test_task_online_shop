import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import Basket, Item, Order


class HomeView(TemplateView):
    """Главная страница"""

    template_name = 'app_products/home.html'


class CatalogListView(ListView):
    """Каталог товаров"""

    model = Item
    context_object_name = 'items'
    template_name = 'app_products/catalog.html'
    paginate_by = 3


@login_required
def add_in_basket(request, item_id):
    """Добавление в корзину товара"""

    Basket.create_or_update(item_id, request.user)
    item = Item.objects.get(id=item_id)
    messages.info(request, message=f'Товар <b>{item.name}</b> добавлен в корзину')

    return redirect(request.META['HTTP_REFERER'])


@login_required
def remove_from_basket(request, basket_id):
    """Удаление товара из корзины"""

    basket = Basket.objects.get(id=basket_id)
    messages.error(request, message=f'Товар <b>{basket.item.name}</b> удален из корзины')
    basket.delete()

    return redirect(request.META['HTTP_REFERER'])


class SaveOrderView(View):
    """Сохранение заказа"""

    def get(self, request):
        """Создаем заказ в БД и обновляем данные корзины пользователя"""

        comment = request.GET.get('comment')
        order = Order.objects.create(
            owner=request.user,
            number=random.randint(1, 10000),
            comment=comment
        )
        messages.info(request, message='Заказ успешно сохранен и отправлен для подтверждения')
        order.update_after_ordering()

        return redirect(reverse('app_users:profile', kwargs={'email': request.user.email}))
