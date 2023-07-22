from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderProduct
from .serializers import OrderSerializer, OrderProductSerializer, OrderProductDetailSerializer, OrderDetailSerializer
from user.permissions import IsOwnerOrAdmin, IsOwnerOrReadOnlyForAdmin

class OrderListCreateView(generics.ListCreateAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderProductListCreateView(generics.ListCreateAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwnerOrReadOnlyForAdmin]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderDetailSerializer
        return OrderSerializer


class OrderProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer