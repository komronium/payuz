from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

from product.models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ("image", "image_thumbnail")
    readonly_fields = ("image_thumbnail",)

    def image_thumbnail(self, obj):
        try:
            img = obj.image
        except Exception:
            img = None
        if img and getattr(img, 'url', None):
            return format_html('<img src="{}" style="height: 60px; width: 60px; object-fit: cover; border-radius:2px;" />', img.url)
        return '-'

    image_thumbnail.short_description = "Rasm"


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name_uz', 'image_thumbnail', 'category', 'price', 'is_active', 'created_at')
    list_display_links = ('id', 'name_uz')
    list_filter = ('is_active', 'created_at', 'category')
    search_fields = ('name', 'name_uz', 'name_ru', 'name_en', 'category__name', 'category__name_uz', 'category__name_ru', 'category__name_en')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = (ProductImageInline,)

    def image_thumbnail(self, obj):
        try:
            image = obj.images.all()[0]
        except Exception:
            image = None
        if image and getattr(image, 'image', None) and hasattr(image.image, 'url'):
            return format_html('<img src="{}" style="height: 60px; width: 60px; object-fit: cover; border-radius:2px;" />', image.image.url)
        return '-'

    image_thumbnail.short_description = 'Rasm'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('images')


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name_uz', 'is_active', 'created_at')
    list_display_links = ('id', 'name_uz')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'name_uz', 'name_ru', 'name_en')
    ordering = ('name_uz',)
    readonly_fields = ('created_at', 'updated_at')
