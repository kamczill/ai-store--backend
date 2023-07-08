import os
import mimetypes

from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView

class GetFileView(APIView):
    def get(self, request, image_name):
        # Path to the image file
        image_path = os.path.join(settings.MEDIA_ROOT + 'files/' + image_name)
        
        # Check if the image file exists
        if not os.path.exists(image_path):
            return HttpResponse('Image not found.', status=404)
        
        # Open the image file in binary mode
        with open(image_path, 'rb') as f:
            # Read the image data
            image_data = f.read()
            
        # Set the appropriate content type for the response
        content_type, _ = mimetypes.guess_type(image_path)
        print(content_type)
        if not content_type:
            content_type = 'application/octet-stream'
        
        # Create the HttpResponse object with the image data and content type
        response = HttpResponse(image_data, content_type=content_type)
        
        return response