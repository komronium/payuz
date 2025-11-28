from rest_framework import serializers

from order.models import Order, OrderItem
from product.models import Product
from product.serializers import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_id', 'quantity', 'total_price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid', 'created_at', 'items')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)

        for item in items_data:
            product_id = int(item.get('product_id'))
            product = Product.objects.get(pk=product_id)
            price = product.price
            quantity = item.get('quantity', 1)
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

        order.save()
        return order
