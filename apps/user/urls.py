from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.views import LoginView, LogoutView, SignUpView

app_name = "user"

urlpatterns = [
    path("users/signup", SignUpView.as_view(), name="user_signup"),
    path("users/login", LoginView.as_view(), name="user_login"),
    path("users/logout", LogoutView.as_view(), name="user_logout"),
    path("users/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
