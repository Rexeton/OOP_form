from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class TemplateForm(forms.Form):
    full_name = forms.CharField()
    subject= forms.CharField()
    # choices в ChoiceField нужен только для отображения в HTML форме
    # my_select = forms.ChoiceField(choices=(
    #     ("begin", "Начальные"),
    #     ("middle", "Средние"),
    #     ("snake_speek", "Разговариваю со змеями"),
    # ))
    # # widget тоже нужен только для отображения в HTML
    Message = forms.CharField(widget=forms.Textarea)
    # my_password = forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField()
    #my_bdate=forms.DateField()
    #my_number=forms.IntegerField()
    #my_chek=forms.BooleanField()