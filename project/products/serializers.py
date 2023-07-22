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
    tax = serializers.IntegerField()
    free = serializers.BooleanField(default=False)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def validate_title(self, value):
        if Product.objects.filter(title=value).exists():
            raise serializers.ValidationError("Product with this title already exists.")
        return value
    
    def validate_description(self, value):
        if Product.objects.filter(description=value).exists():
            raise serializers.ValidationError("Product with this description already exists.")
        return value

class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= '__all__'

