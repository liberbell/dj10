from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("Needs to start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    # botcacher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data["email"]
        vmail = all_clean_data["verify_email"]
        
        if email != vmail:
            raise forms.ValidationError("Make sure emails match")

    # def clean_botcacher(self):
    #     botcacher = self.cleaned_data["botcacher"]
    #     if len(botcacher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcacher