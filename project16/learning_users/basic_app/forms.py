from django import forms
from basic_app.models import UserProfileInfoModel

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = UserProfileInfoModel
        exclude = ('user', )