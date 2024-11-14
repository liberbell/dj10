from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index', views.index, name="firstapp_index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)