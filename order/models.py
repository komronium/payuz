from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name="Mijoz ismi")
    phone_number = models.CharField(max_length=25, verbose_name="Telefon raqam", null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name="Manzil")
    total_cost = models.IntegerField(verbose_name="Umumiy narx")
    payment_method = models.CharField(max_length=255, verbose_name="To‘lov turi")
    is_paid = models.BooleanField(default=False, verbose_name="To‘langan?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"

    def __str__(self):
        return f"Buyurtma #{self.id}"
