from django.contrib import admin
from django.contrib.auth.models import User, Group

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ('product', 'quantity', 'price', 'total_price')
    readonly_fields = ('product', 'quantity', 'price', 'total_price')
    raw_id_fields = ('product',)
    can_delete = False

    def has_add_permission(self, request, obj):
        # Prevent inline adding from the order admin; items should be created through API
        # or a separate admin flow.
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid')
    list_display_links = ('id', 'customer_name')
    list_filter = ('is_paid', 'payment_method')
    search_fields = ('id', 'customer_name', 'phone_number', 'address', 'payment_method')
    ordering = ('-created_at', )
    readonly_fields = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid', 'created_at')
    inlines = (OrderItemInline,)

    has_add_permission = lambda *_: False
    has_delete_permission = lambda *_: False


admin.site.unregister(User)
admin.site.unregister(Group)



# Customize admin texts
admin.site.site_header = "Gijduvan Crafts boshqaruv paneli"
admin.site.site_title = "Gijduvan Crafts admin"
admin.site.index_title = "Boshqaruv bo'limlari"
