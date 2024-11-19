from django.shortcuts import render
from appTwo.models import Users

# Create your views here.
def index(request):
    return render(request, "appthree/index.html")