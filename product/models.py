from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi")
    is_active = models.BooleanField(default=True, verbose_name="Aktivmi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ("name", )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name="Kategoriya",
    )
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    description = models.TextField(blank=True, verbose_name="Ta'rif")
    price = models.PositiveIntegerField(verbose_name="Narx")
    is_active = models.BooleanField(default=True, verbose_name="Aktivmi?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
        ordering = ("-created_at", )

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Mahsulot",
    )
    image = models.ImageField(upload_to='products/', verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Mahsulot rasmi"
        verbose_name_plural = "Mahsulot rasmlari"
        ordering = ('-created_at', )

    def __str__(self):
        return f"{self.product.name} rasmi"
