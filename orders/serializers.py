from rest_framework import serializers
from .models import CartItem, Order, OrderItem
from products.serializers import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """adding product_id field with queryset to avoid circular import"""
        self.fields['product_id'] = serializers.PrimaryKeyRelatedField(
            queryset=self.Meta.model._meta.get_field('product').remote_field.model.objects.all(),
            source='product',
            write_only=True
        )

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'order_items', 'created_at']