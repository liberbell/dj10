from django.shortcuts import render
from appTwo.models import User
from django.http import HttpResponse
from appTwo.forms import NewUser

# Create your views here.
def index(request):
    return render(request, "appthree/index.html")

def users(request):
    
    