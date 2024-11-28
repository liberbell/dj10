from django.urls import path
from . import views

urlpatterns = [
    path("other", views.other, name="other"),
]
