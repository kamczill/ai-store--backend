from user import views
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('create/', views.UserCreate.as_view()),
    path('refresh/', views.RefreshView.as_view(), name='refresshhhh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('me/', views.CurrentUser.as_view(), name='current_user'),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('<int:id>/purchases', views.UserPurchasesListView.as_view(), name='user_purchases'),
    path('e-book/', views.EbookView.as_view(), name='e-book'),
]
