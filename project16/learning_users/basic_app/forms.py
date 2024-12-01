from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

class UserProfileInfo(forms.ModelForm):
    
    class Meta:
        model = UserProfileInfoModel