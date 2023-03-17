from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'is_staff')
    list_filter = ('is_staff', )
    search_fields = ('email',)


admin.site.register(User, UserAdmin)
