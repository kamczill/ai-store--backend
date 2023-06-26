from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView, token_refresh
from rest_framework_simplejwt.exceptions import TokenError
from django.middleware import csrf
from django.http import HttpRequest, FileResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status, generics
from .models import User
from .serializers import UserSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import IsAuthenticated

from .authenticate import CustomAuthentication


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class LoginView(APIView):
    authentication_classes = []
    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request, format=None):
        data = request.data
        response = Response()        
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                    value = data["access"],
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                response.set_cookie(
                    key = 'refresh_token', 
                    value = data["refresh"],
                    expires = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                response.set_cookie(
                    key = 'logged_in', 
                    value = 'true',
                    expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly = False,
                    samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {"Success" : "Login successfully","data":data}
                return response
            else:
                return Response({"No active" : "This account is not active!!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid" : "Invalid username or password!!"}, status=status.HTTP_404_NOT_FOUND)

class RefreshView(TokenRefreshView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if(refresh_token):
            try:
                new_access_token = RefreshToken(refresh_token).access_token
            except:
                return Response({"message": "Refresh Token is invalid or expired"}, status=status.HTTP_401_UNAUTHORIZED)
            
            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(
                        key = settings.SIMPLE_JWT['AUTH_COOKIE'], 
                        value = new_access_token,
                        expires = settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                        secure = settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                        httponly = settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                        samesite = settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                    )
        else :
            return Response(status=status.HTTP_404_NOT_FOUND)
        return response
    
class LogoutView(APIView):
    authentication_classes = []
    
    def get(self, request):
        response = Response({"message": "You are logout succesfully!"}, status=status.HTTP_202_ACCEPTED)
        for cookie in ['access_token', 'refresh_token', 'logged_in']:
            response.delete_cookie(cookie)
        return response


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CustomAuthentication]


class UserCreate(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={201: UserSerializer},
    )
    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response({'message': 'User registered successfully.'})
        return Response(user.errors, status=400)

class CurrentUser(generics.RetrieveAPIView):
    # @extend_schema(
    #     request=UserSerializer,
    #     responses={200: UserSerializer},
    # )
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message": "You're not logged in!"},status=status.HTTP_401_UNAUTHORIZED)
            
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class EbookView(APIView):
    def get(self, request):
        if request.user.id:
            response = FileResponse(open('files/e-book.pdf', 'rb'))
            return response