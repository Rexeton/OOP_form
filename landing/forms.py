from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class TemplateForm(forms.Form):
    Full_name = forms.CharField()
    Subject= forms.CharField()
    Message = forms.CharField(widget=forms.Textarea)
    Email=forms.EmailField()
