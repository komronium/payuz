from rest_framework import serializers

from order.models import Order, OrderItem
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    # `total_price` is a property on the model; do not specify `source` since it's
    # the same as the field name — specifying `source` redundantly raises an
    # AssertionError in DRF.
    total_price = serializers.IntegerField(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'quantity', 'total_price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'phone_number', 'address', 'total_cost', 'payment_method', 'is_paid', 'created_at', 'items')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        # Create the order
        order = Order.objects.create(**validated_data)

        for item in items_data:
            product = item.get('product')
            if isinstance(product, int):
                product = Product.objects.get(pk=product)
            # default unit price from product snapshot if not provided
            price = product.price
            quantity = item.get('quantity', 1)
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

        order.save()
        return order
