from django.shortcuts import render
from django.http import HttpResponse

def caseload(request):
    return render(request, 'caseload/dashboard.html')

