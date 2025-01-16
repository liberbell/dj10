from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    return render(request, "index.html")

class CBView(View):
    def get(self, request):
        return HttpResponse("Class Based View Are Cool.")
    
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["injectme"] = "BASIC Injection!"
        return context
    
class IndexView(TemplateView):
    template_name = "index.html"
    
class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'basic_app/school_detail.html'