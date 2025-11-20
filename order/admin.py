from django.contrib import admin
from django.contrib.auth.models import User, Group

from order.models import Order


@admin.register(Order)
class  OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid')
    list_display_links = ('id', 'customer_name')
    list_filter = ('is_paid', 'payment_method')
    search_fields = ('id', 'customer_name', 'phone_number', 'address', 'payment_method')
    ordering = ('-created_at', )
    readonly_fields = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid', 'created_at')

    has_add_permission = lambda *_: False
    has_delete_permission = lambda *_: False


admin.site.unregister(User)
admin.site.unregister(Group)


# Customize admin texts
admin.site.site_header = "Gijduvan Crafts boshqaruv paneli"
admin.site.site_title = "Gijduvan Crafts admin"
admin.site.index_title = "Boshqaruv bo'limlari"


