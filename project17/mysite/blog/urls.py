from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.AboutView, name="about"),
]