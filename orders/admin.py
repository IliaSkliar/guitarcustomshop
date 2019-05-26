from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'master', 'problem', 'status', 'created_at', 'updated_at',)
    list_filter = ('status',)


admin.site.register(Order, OrderAdmin)
