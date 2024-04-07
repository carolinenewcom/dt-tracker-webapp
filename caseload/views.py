from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm

from django.contrib import auth, messages 

def caseload(request):
    return render(request, 'caseload/caseload.html')

def schedule(request):
    return render(request, 'caseload/schedule.html')

def sessions(request):
    return render(request, 'caseload/sessions.html')

def attendance(request):
    return render(request, 'caseload/attendance.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid login information. Please try again.')
    return render(request, 'caseload/login.html', {'form': LoginForm})
    