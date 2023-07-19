from rest_framework import serializers
from .models import Order, OrderProduct
from products.serializers import ProductGetSerializer

class OrderProductSerializer(serializers.ModelSerializer):
    # product = ProductGetSerializer(read_only=True)
    class Meta:
        model = OrderProduct
        fields = ['order', 'product']

class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True, source='orderproduct_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'purchase_timestamp', 'products']

class OrderProductDetailSerializer(serializers.ModelSerializer):
    product = ProductGetSerializer(read_only=True)
    class Meta:
        model = OrderProduct
        fields = ['order', 'product']

class OrderDetailSerializer(serializers.ModelSerializer):
    products = OrderProductDetailSerializer(many=True, read_only=True, source='orderproduct_set')

    class Meta:
        model = Order
        fields = ['id', 'user', 'purchase_timestamp', 'products']
