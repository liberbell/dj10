from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {"insert_me": "Hello I am comming from first_app/index.html!"}
    my_dict2 = {"insert_content": "Hello I am from first app!"}
    return render(request, "first_app/index.html", context=my_dict2)