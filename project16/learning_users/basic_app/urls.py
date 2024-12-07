from django.urls import path, re_path
from . import views

app_name = "basic_app"

urlpatterns = [
    path('register', views.register, name="register"),
    re_path('user_login/$', views.user_login, name="user_login"),
]