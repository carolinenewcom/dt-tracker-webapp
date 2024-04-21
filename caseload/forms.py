import datetime

from django import forms
from django.forms import ModelForm
from .models import Child, Schedule

from django.core.exceptions import ValidationError
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
    

#class AddSession(forms.Form):
    #session_date_log = forms.DateField(help_text="Enter the date of session.")

    #def clean_renewal_date(self):
        #data = self.clean_session_date_data['session_date_log']

        # Check if a date is a future date.
        #if data > datetime.date.today():
            #raise ValidationError(_('Invalid date - Session must have been completed today or before.'))

        # Remember to always return the cleaned data.
        #return data