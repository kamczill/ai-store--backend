from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import ProductCreateSerializer, ProductGetSerializer
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from .models import Product

class ProductCreateView(APIView):
    permission_classes = [IsAdminUser]
    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'cover': {
                        'type': 'string',
                        'format': 'binary'
                    },
                    'title': {
                        'type': 'string',
                        'maxLength': 100
                    },
                    'author': {
                        'type': 'string',
                        'maxLength': 100
                    },
                    'description': {
                        'type': 'string'
                    },
                    'net_price': {
                        'type': 'number',
                        'format': 'decimal',
                        'maximum': 9999.99,
                        'minimum': 0
                    }
                },
                'required': ['cover', 'title', 'author', 'description', 'net_price']
            }
        },
        responses={201: ProductCreateSerializer},
        methods=["POST"]
    )
    def post(self, request, format=None):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Form submitted successfully.'}, status=201)
        else:
            return Response(serializer.errors, status=400)
        
class ProductsGetView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductGetSerializer
    permission_classes = []

class ProductGetView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductGetSerializer
    permission_classes = []