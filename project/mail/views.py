from rest_framework.views import APIView
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from .serializers import MailSerializer

# Create your views here.

class EmailAPI(APIView):
    authentication_classes = []
    @extend_schema(
        # parameters=[MailSerializer],
        responses={201: MailSerializer},
    )
    
    def get(self, request):
        email = EmailMessage(
            "Hello",
            "Bardzo cieszymy się, że dołączyłeś do nas. Zostawiamy e-book w ramach podziękowania!",
            'bot.aiswiat@int.pl',
            ['kam134@o2.pl'],
        )
        email.attach_file('files/e-book.pdf')
        email.send()
        # send_mail(
        #         'Gratulujemy dolaczenia do nas!',
        #         'Udalo ci sie zarejestrowac szefie!',
        #         'bot.aiswiat@int.pl',
        #         ['kam134@o2.pl']
        #     )
        return Response('ok', status=200)
