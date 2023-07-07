from django.urls import path
from .views import ProductCreateView, ProductsGetView, ProductGetView

urlpatterns = [
    # Your other URL patterns
    path('', ProductsGetView.as_view(), name='get-products'),
    path('<pk>', ProductGetView.as_view(), name='get-products'),
    path('create/', ProductCreateView.as_view(), name='product-upload'),
]