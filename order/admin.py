from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html

from order.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ('product', 'product_thumbnail', 'quantity', 'price', 'total_price')
    readonly_fields = ('product', 'product_thumbnail', 'quantity', 'price', 'total_price')
    raw_id_fields = ('product',)
    can_delete = False

    def has_add_permission(self, request, obj):
        # Prevent inline adding from the order admin; items should be created through API
        # or a separate admin flow.
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def product_thumbnail(self, obj):
        """Render a small thumbnail of the product's first image, or '-' if none."""
        try:
            image = obj.product.images.all()[0]
        except Exception:
            image = None
        if image and getattr(image, 'image', None) and hasattr(image.image, 'url'):
            return format_html('<img src="{}" style="height:40px; border-radius:4px;" />', image.image.url)
        return '-'

    product_thumbnail.short_description = 'Rasm'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('product').prefetch_related('product__images')


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


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product_thumbnail", "product", "order", "quantity", "price", "total_price")
    readonly_fields = ("product_thumbnail", "total_price")
    raw_id_fields = ("product", "order")

    def product_thumbnail(self, obj):
        try:
            image = obj.product.images.all()[0]
        except Exception:
            image = None
        if image and getattr(image, 'image', None) and hasattr(image.image, 'url'):
            return format_html('<img src="{}" style="height:40px; border-radius:4px;" />', image.image.url)
        return '-'

    product_thumbnail.short_description = 'Rasm'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('product', 'order').prefetch_related('product__images')
