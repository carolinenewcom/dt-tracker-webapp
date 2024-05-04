from django import forms
from django.forms import ModelForm, TextInput
from .models import Child, Schedule, SessionAttendance

from django.utils.translation import gettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class AddChild(ModelForm):
    class Meta:
        model = Child
        fields = '__all__'
        labels = {
            'id_number': '',
            'first_name': '',
            'last_name': '',
            'user': '',

        }
        widgets = {
            'id_number': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Child ID'
                }),
            'first_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                })
        }

class AddSchedule(ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
        labels = {
            'scheduled_week_day': '',
            'session_time': '',
            'child': '',
        }
        widgets = {
            'scheduled_week_day': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Scheduled Day'
                }),
            'session_time': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Session Time 00:00'
                })
        }


class NewSessionLog(ModelForm):
    class Meta:
        model = SessionAttendance
        fields = '__all__'
        labels = {
            'child': '',
            'session_date': '',
            'session_attendance': '',
        }
        widgets = {
            'month': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': ''
                }),
            'sessions_completed': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '',
                'min':0,
                'max':5,
                'type': 'number'
                }),
            'excused_absence': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '',
                'min':0,
                'max':5,
                'type': 'number'
                }),
            'unexcused_absence': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': '',
                'min':0,
                'max':5,
                'type': 'number'
                })
        }