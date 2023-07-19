from rest_framework import serializers
from .models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['order', 'product']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True, source='orderproduct_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'purchase_timestamp', 'products']
