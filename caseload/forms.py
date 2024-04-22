from django import forms
from django.forms import ModelForm
from .models import Child, Schedule

from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddChild(ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

class AddSchedule(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
    