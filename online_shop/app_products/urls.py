from django.urls import path

from .views import (CatalogListView, HomeView, SaveOrderView, add_in_basket,
                    remove_from_basket)

app_name = 'app_products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('catalog/page/<int:page>/', CatalogListView.as_view(), name='paginator'),
    path('basket/add/<int:item_id>', add_in_basket, name='add_in_basket'),
    path('basket/remove/<int:basket_id>', remove_from_basket, name='delete_from_basket'),
    path('create-order/', SaveOrderView.as_view(), name='save_order'),
]
