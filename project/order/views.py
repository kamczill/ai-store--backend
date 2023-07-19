from rest_framework import generics
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProductListCreateView(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer