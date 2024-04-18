from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, AddChild
from .models import Child
from django.db.models import Q


import datetime

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import auth, messages 

def caseload(request):
    all_children = Child.objects.all
    return render(request, 'caseload/caseload.html', {'all':all_children})

def schedule(request):
    return render(request, 'caseload/schedule.html')

def sessions(request):
    all_children = Child.objects.all
    return render(request, 'caseload/sessions.html', {'all':all_children})

def attendance(request):
    return render(request, 'caseload/attendance.html')

def search_caseload(request):
    if request.method == "POST":
        searched = request.POST['searched']
        child = Child.objects.filter(
            Q(first_name__icontains=searched) | Q(last_name__icontains=searched)
            )
        return render(request, 'caseload/search_caseload.html', {'searched': searched, 'child': child})
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

def new_child(request):
    form = AddChild()
    if request.method == "POST":
        form = AddChild(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'caseload/new_child.html', {'form': form})
 

def delete_child(request, child_id):
    if request.method == "POST":
        d_child= Child.objects.get(id=child_id)
        d_child.delete()
        return redirect('/')
    dele = Child.objects.get(id=child_id)
    dele.delete()
    return redirect('/')    


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

