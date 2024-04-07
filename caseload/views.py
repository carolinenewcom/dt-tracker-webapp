from django.shortcuts import render
from django.http import HttpResponse

def caseload(request):
    return render(request, 'caseload/caseload.html')

def schedule(request):
    return render(request, 'caseload/schedule.html')

def sessions(request):
    return render(request, 'caseload/sessions.html')

def attendance(request):
    return render(request, 'caseload/attendance.html')