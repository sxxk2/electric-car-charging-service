from django.urls import path

from apps.user.views import LoginView, LogoutView, SignUpView

app_name = "user"

urlpatterns = [
    path("/signup", SignUpView.as_view(), name="user_signup"),
    path("/login", LoginView.as_view(), name="user_login"),
    path("/logout", LogoutView.as_view(), name="user_logout"),
]
