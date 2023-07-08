from rest_framework import serializers
from django.utils import timezone
from django.forms.fields import FileField
from .models import Product

class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField()
    net_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    cover = serializers.FileField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'