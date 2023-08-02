from rest_framework import serializers
from django.conf import settings
from django.utils import timezone
from django.forms.fields import FileField
from .models import Product
import boto3
class ProductCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField()
    net_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    cover = serializers.FileField()
    tax = serializers.IntegerField(default=5)
    free = serializers.BooleanField(default=False)
    file_path = serializers.FileField()
    is_downloadable = serializers.BooleanField(default=False)





    def create(self, validated_data):
        cover_file = validated_data.pop('cover')
        file_path_file = validated_data.pop('file_path')

        # Store just the filenames in the model
        validated_data['cover'] = 'files/' + cover_file.name
        validated_data['file_path'] = 'files/products/' + file_path_file.name

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

