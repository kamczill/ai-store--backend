from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .serializers import ProductCreateSerializer, ProductGetSerializer
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from .models import Product
import boto3

class ProductCreateView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser]

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
                    },
                    'tax': {
                    'type': 'integer',
                    'minimum': 0,
                    'maximum': 100
                    },
                     'free': {
                    'type': 'boolean',
                    },
                    'file_path': {
                        'type': 'string',
                        'format': 'binary'
                    },
                     'is_downloadable': {
                    'type': 'boolean',
                    },
                },
                'required': ['cover', 'title', 'author', 'description', 'net_price', 'free', 'tax', 'file_path', 'is_downloadable']
            }
        },
        responses={201: ProductCreateSerializer},
        methods=["POST"]
    )
    def post(self, request, format=None):
        serializer = ProductCreateSerializer(data=request.data)
        if serializer.is_valid():
            s3 = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
                )
            try:
                file = request.data['file_path']
                cover = request.data['cover']
                s3.put_object(Bucket='aiszef', Key='products/' + file.name, Body=file.read())
                s3.put_object(Bucket='aiszef', Key='covers/' + cover.name, Body=cover.read())
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
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
    