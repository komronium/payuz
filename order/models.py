from django.db import models

from product.models import Product


class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name="Mijoz ismi")
    phone_number = models.CharField(max_length=25, verbose_name="Telefon raqam", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Manzil")
    total_cost = models.PositiveIntegerField(verbose_name="Umumiy narx")
    payment_method = models.CharField(max_length=255, verbose_name="To‘lov turi")
    is_paid = models.BooleanField(default=False, verbose_name="To‘langan?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"

    def __str__(self):
        return f"Buyurtma #{self.id}"


class OrderItem(models.Model):
    """Represents a single product and quantity inside an Order.

    Storing the `price` on the item keeps a snapshot of the unit price at the
    time of order creation and avoids inconsistencies if Product price changes.
    """

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Buyurtma",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items',
        verbose_name="Mahsulot",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="Soni")
    price = models.PositiveIntegerField(verbose_name="Narx (snapshot)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Buyurtma mahsuloti"
        verbose_name_plural = "Buyurtma mahsulotlari"
        ordering = ("-id",)

    def __str__(self):
        return f"#{self.id} — {self.product.name} x{self.quantity}"

    @property
    def total_price(self) -> int:
        """Total price for this line (quantity * unit price)."""
        return self.price * self.quantity

