from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_record": webpages_list}
    my_dict = {"insert_me": "Hello I am comming from first_app/index.html!"}
    my_dict2 = {"insert_content": "Hello I am from first app!"}
    return render(request, "first_app/index.html", context=my_dict2)