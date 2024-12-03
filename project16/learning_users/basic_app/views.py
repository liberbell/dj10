from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfo

# Create your views here.
def index(request):
    return render(request, "basic_app/index.html")

def register(request):
    registerd = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)
    return render(request, "basic_app/register.html")