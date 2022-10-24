from accounts.views import login_user, user_logout
from django.urls import path

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", user_logout, name="logout"),
]
