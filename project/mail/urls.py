
from django.contrib import admin
from django.urls import path
from .views import EmailAPI

urlpatterns = [
    path('send-email', EmailAPI.as_view()),
]