from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import Child


import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import auth, messages 

def caseload(request):
    return render(request, 'caseload/caseload.html')

def schedule(request):
    return render(request, 'caseload/schedule.html')

def sessions(request):
    return render(request, 'caseload/sessions.html')

def attendance(request):
    return render(request, 'caseload/attendance.html')

def search_caseload(request):
    if request.method == "POST":
        searched = request.POST['searched']
        #child = Child.objects.filter(id__contains=searched)

        return render(request, 'caseload/search_caseload.html', {'searched': searched}) #{'child': child})
    else:
        return render(request, 'caseload/search_caseload.html')

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




#def add_session_log(request, pk):
    #session_instance = get_object_or_404(SessionInstance, pk=pk)

    # If this is a POST request then process the Form data
    #if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        #form = AddSession(request.POST)

        # Check if the form is valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #session_instance.session_date = form.cleaned_data['session_date_log']
            #session_instance.save()

            # redirect to a new URL:
            #return HttpResponseRedirect(reverse('session log entered'))

    # If this is a GET (or any other method) create the default form.
    #else:
        #context = {
        #'form': form,
        #'session_instance': session_instance,
    #}

   # return render(request, 'caseload/sessions.html', context) 

