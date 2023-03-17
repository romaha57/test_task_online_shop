from django.contrib import admin

from .models import Basket, Item, Order


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name',)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity')
    list_filter = ('created_at',)
    search_fields = ('item',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'status', 'owner', 'admin_confirm', 'admin_reject')
    list_editable = ('status', 'admin_confirm', 'admin_reject')
    list_filter = ('created_at', 'status')
    search_fields = ('owner',)

    raw_id_fields = ('admin_confirm', 'admin_reject')


admin.site.register(Item, ItemAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Order, OrderAdmin)
