from django.urls import path
from appTwo import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path("users/", views.users, name="users"),
]