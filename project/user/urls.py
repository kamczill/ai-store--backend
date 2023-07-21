from user import views
from django.urls import path, include
from django_rest_passwordreset.views import ResetPasswordRequestToken, ResetPasswordConfirm


urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('create/', views.UserCreate.as_view()),
    path('refresh/', views.RefreshView.as_view(), name='refresshhhh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('change-password/', views.ChangePasswordView.as_view(), name='logout'),
    path('reset_password/', ResetPasswordRequestToken.as_view(), name='reset-password-request'),

    # confirm the token and allow user to set new password
    path('reset_password/confirm/', ResetPasswordConfirm.as_view(), name='reset-password-confirm'),
    path('me/', views.CurrentUser.as_view(), name='current_user'),
    path('me/orders/', views.CurrentUserOrderList.as_view(), name='current_user_orders'),
    path('<int:pk>/', views.UserDetail.as_view()),
    path('e-book/', views.EbookView.as_view(), name='e-book'),
]
