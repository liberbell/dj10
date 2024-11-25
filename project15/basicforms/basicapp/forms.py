from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcacher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    # def clean_botcacher(self):
    #     botcacher = self.cleaned_data["botcacher"]
    #     if len(botcacher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcacher