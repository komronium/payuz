from rest_framework import serializers

from product.models import Category, Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = (
            'id',
            'image',
            'created_at',
        )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'name_uz',
            'name_ru',
            'name_en',
            'is_active',
            'created_at',
            'updated_at',
        )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'description',
            'name_uz',
            'name_ru',
            'name_en',
            'description_uz',
            'description_ru',
            'description_en',
            'price',
            'is_active',
            'created_at',
            'updated_at',
            'images',
        )
