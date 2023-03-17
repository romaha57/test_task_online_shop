from django.template import Library

from app_products.models import Basket


register = Library()


@register.inclusion_tag('app_products/basket.html')
def show_basket(user):
    """Тег шаблона для отображения корзины товаров"""

    baskets = Basket.objects.filter(user=user)
    return {'baskets': baskets}