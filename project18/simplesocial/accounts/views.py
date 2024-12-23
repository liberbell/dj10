from django.shortcuts import render
from django.core import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")