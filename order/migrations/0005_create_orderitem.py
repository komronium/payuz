"""Create OrderItem model.

This migration introduces the OrderItem model and its fields.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0004_alter_order_total_cost"),
        ("product", "0004_category_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantity", models.PositiveIntegerField(default=1, verbose_name="Soni")),
                ("price", models.PositiveIntegerField(verbose_name="Narx (snapshot)")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")),
                ("order", models.ForeignKey(on_delete=models.CASCADE, related_name="items", to="order.order", verbose_name="Buyurtma")),
                ("product", models.ForeignKey(on_delete=models.PROTECT, related_name="order_items", to="product.product", verbose_name="Mahsulot")),
            ],
            options={
                "verbose_name": "Buyurtma mahsuloti",
                "verbose_name_plural": "Buyurtma mahsulotlari",
                "ordering": ("-id",),
            },
        ),
    ]
