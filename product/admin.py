from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from product.models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name_uz', 'category', 'price', 'is_active', 'created_at')
    list_display_links = ('id', 'name_uz')
    list_filter = ('is_active', 'created_at', 'category')
    search_fields = ('name', 'name_uz', 'name_ru', 'name_en', 'category__name', 'category__name_uz', 'category__name_ru', 'category__name_en')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = (ProductImageInline,)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name_uz', 'is_active', 'created_at')
    list_display_links = ('id', 'name_uz')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'name_uz', 'name_ru', 'name_en')
    ordering = ('name_uz',)
    readonly_fields = ('created_at', 'updated_at')
