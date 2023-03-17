import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Item(models.Model):
    """Модель товара"""

    name = models.CharField(max_length=200, verbose_name='название товара')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена товара')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class BasketQuerySet(models.QuerySet):
    """Класс для обращения к общим методам всех корзин товаров"""

    def total_sum(self):
        """Возвращает общую стомость всех товаров в корзине пользователя"""

        return sum((basket.sum_items() for basket in self))

    def total_quantity(self):
        """Возвращает общее количество всех товаров в корзине пользователя"""

        return sum((basket.quantity for basket in self))


class Basket(models.Model):
    """Модель корзины товаров пользователя"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='корзина для пользователя')
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='товар')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='количество товара в корзине')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    objects = BasketQuerySet.as_manager()

    def sum_items(self):
        """Возвращает общую стоиомсть каждого отдельного товара в корзине"""

        return self.quantity * self.item.price

    @classmethod
    def create_or_update(cls, item_id, user):
        """Создаем новую корзину или увеличиаем количество в уже существующей"""

        item = Item.objects.get(id=item_id)
        baskets = Basket.objects.filter(user=user, item=item)

        # если такого товара у пользователя нет, то создаем
        if not baskets.exists():
            basket = Basket.objects.create(
                user=user,
                item=item,
                quantity=1
            )

        # иначе добавляем количество данного товара
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()

        return basket

    def history_in_json(self):
        """Заполняет словарь для хранения истории заказа"""

        history_json = {
            'product_name': self.item.name,
            'quantity': self.quantity,
            'price': float(self.item.price),
            'total_price': float(self.sum_items())
        }
        return history_json

    def __str__(self):
        return f'Корзина - {self.user.email}'

    class Meta:
        ordering = ('user',)
        verbose_name = 'корзина товара'
        verbose_name_plural = 'корзина товаров'


class Order(models.Model):
    """Модель заказа"""

    CREATED_ORDER = 1
    CONFIRMED = 2
    REJECTED = 3
    STATUS_CHOICES = (
        (CREATED_ORDER, 'создан'),
        (CONFIRMED, 'подтвержден'),
        (REJECTED, 'отклонен'),
    )

    number = models.PositiveIntegerField(verbose_name='номер заказа')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='владелец заказа')
    comment = models.CharField(max_length=255, verbose_name='комментарий к заказу', blank=True, null=True)
    status = models.SmallIntegerField(default=CREATED_ORDER, choices=STATUS_CHOICES)
    basket_history = models.JSONField(default=dict, verbose_name='история корзины')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата формирования заказа')
    confirmed_at = models.DateTimeField(verbose_name='дата подтверждения', blank=True, null=True)
    rejected_at = models.DateTimeField(verbose_name='дата отклонения', blank=True, null=True)
    admin_confirm = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='подтвердил админ',
                                      related_name='admin_confirm', blank=True, null=True)
    admin_reject = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='отклонил админ',
                                     related_name='admin_reject', blank=True, null=True)
    comment_for_reject = models.TextField(default='Уточняется', verbose_name='комментарий при отклонении')

    def update_after_ordering(self):
        """После сохранения заказа: сохраняем историю корзины в заказе и удаляем товары из корзины пользователя"""

        baskets = Basket.objects.filter(user=self.owner)
        self.basket_history = {
            'items': [basket.history_in_json() for basket in baskets],
            'total_sum': float(baskets.total_sum())
        }
        self.save()
        baskets.delete()

    def __str__(self):
        return f'{self.owner}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """Обновляем время заказа при изменении статуса"""

        if self.status == 2:
            self.confirmed_at = datetime.datetime.utcnow()
        elif self.status == 3:
            self.rejected_at = datetime.datetime.utcnow()

        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
