from accounts.views import login_user, user_logout, signup
from django.urls import path

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", signup, name="signup"),
]
