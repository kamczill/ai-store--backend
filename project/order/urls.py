from django.urls import path
from .views import OrderListCreateView, OrderDetailView, OrderProductListCreateView, OrderProductDetailView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order-products/', OrderProductListCreateView.as_view(), name='orderproduct-list-create'),
    path('order-products/<int:pk>/', OrderProductDetailView.as_view(), name='orderproduct-detail'),
]
