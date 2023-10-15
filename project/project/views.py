import os
import mimetypes
import boto3

from django.conf import settings
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from products.models import Product
from order.models import Order, OrderProduct

class GetFileView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, image_name):
        # Path to the image file
        try:
            s3 = boto3.client('s3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    )
            
            # image_path = os.path.join(settings.MEDIA_ROOT + 'files/' + image_name)
            file_obj = s3.get_object(Bucket=settings.AWS_BUCKET_NAME, Key='covers/' + image_name)

            file_content = file_obj['Body'].read()
            # Determine the content type (you may want to refine this)
            content_type = file_obj.get('ContentType', 'application/octet-stream')

            # Create and return the HttpResponse
            response = HttpResponse(file_content, content_type=content_type)
            return response
        except:
            return Response({"message": "not found"}, status=404)
    
class GetPDFFileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pdf_name):
        user = request.user.id
        queryset1 = Product.objects.filter(file_path__icontains=pdf_name).first()
        product_id = queryset1.id
        product_is_free = queryset1.free
        queryset2 = Order.objects.filter(user=user).all()
        order_ids = queryset2.values_list('id', flat=True)
        order_ids_list = list(order_ids)
        queryset3 = OrderProduct.objects.filter(order__in=order_ids_list, product=product_id).first()
        if not product_is_free and not queryset3:
            return HttpResponse('Unauthorized', status=401)
       
        try:
            s3 = boto3.client('s3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    )
            
            file_obj = s3.get_object(Bucket=settings.AWS_BUCKET_NAME, Key='products/' + pdf_name)

            file_content = file_obj['Body'].read()

            content_type = file_obj.get('ContentType', 'application/octet-stream')

            response = HttpResponse(file_content, content_type=content_type)
            return response
        except:
            return Response({"message": "not found"}, status=404)
       