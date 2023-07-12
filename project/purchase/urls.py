from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PurchaseViewSet

router = DefaultRouter()
router.register(r'', PurchaseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]