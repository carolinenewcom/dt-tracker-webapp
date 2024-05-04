from django.shortcuts import render, redirect
from .forms import LoginForm, AddChild, AddSchedule, NewSessionLog
from .models import Child, Schedule, SessionAttendance
from django.db.models import Q
from django.contrib import messages

from django.contrib import auth, messages 

def caseload(request):
    all_children = Child.objects.all
    return render(request, 'caseload/caseload.html', {'all':all_children})

def schedule(request):
    all_schedule = Schedule.objects.all
    return render(request, 'caseload/schedule.html', {'all_schedule':all_schedule})

def sessions(request):
    all_children = Child.objects.all
    return render(request, 'caseload/sessions.html', {'all':all_children})

def attendance(request):
    attendance = SessionAttendance.objects.all
    return render(request, 'caseload/attendance.html', {'attendance':attendance})

def percentage_report(request):
    if request.method == "POST":
        search = request.POST['search']
        data = SessionAttendance.objects.filter(
            Q(month__icontains=search)
            ).order_by('child__first_name')
        return render(request, 'caseload/percentage_report.html', {'search': search, 'data': data})
    else:
        return render(request, 'caseload/percentage_report.html')

def search_caseload(request):
    if request.method == "POST":
        searched = request.POST['searched']
        child = Child.objects.filter(
            Q(first_name__icontains=searched) | Q(last_name__icontains=searched)
            )
        return render(request, 'caseload/search_caseload.html', {'searched': searched, 'child': child})
    else:
        return render(request, 'caseload/search_caseload.html')
    
def search_sessions(request):
    if request.method == "POST":
        searched = request.POST['searched']
        sessionLogs = SessionAttendance.objects.filter(
            Q(child__first_name__icontains=searched) | Q(child__last_name__icontains=searched) | Q(child__id_number__icontains=searched)
            )
        return render(request, 'caseload/search_sessions.html', {'searched': searched, 'sessionLogs': sessionLogs})
    else:
        messages.success(request, 'Information entered was invalid. Please try again.')
        return redirect(request, 'caseload/search_sessions.html')
    
def search_percentage_report(request):
    if request.method == "POST":
        search = request.POST['search']
        data = SessionAttendance.objects.filter(
            Q(child__first_name__icontains=search) | Q(child__last_name__icontains=search) | Q(child__id_number__icontains=search)
            )
        return render(request, 'caseload/search_percentage_report.html', {'search': search, 'data': data})
    else:
        return render(request, 'caseload/search_percentage_report.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid login information. Please try again.')
    return render(request, 'caseload/login.html', {'form': LoginForm})

def new_child(request):
    form = AddChild()
    if request.method == "POST":
        form = AddChild(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Child Has Successfully Been Added To Your Caseload!')
        return redirect('/')
    return render(request, 'caseload/new_child.html', {'form': form})
 

def delete_child(request, child_id):
    if request.method == "POST":
        d_child= Child.objects.get(id=child_id)
        d_child.delete()
        return redirect('/')
    dele = Child.objects.get(id=child_id)
    dele.delete()
    messages.success(request, 'Child Has Successfully Been Deleted From Your Caseload!')
    return redirect('/')   

def new_schedule(request):
    form = AddSchedule()
    if request.method == "POST":
        form = AddSchedule(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Session Has Successfully Been Added To Your Schedule!')
        return redirect('/')
    return render(request, 'caseload/new_schedule.html', {'form': form}) 

def delete_schedule(request, child_id):
    if request.method == "POST":
        d_schedule= Schedule.objects.get(id=child_id)
        d_schedule.delete()
        return redirect('/')
    dele = Schedule.objects.get(id=child_id)
    dele.delete()
    messages.success(request, 'Session Has Successfully Been Deleted From Your Schedule!')
    return redirect('/')  

def delete_session_log(request, child_id):
    if request.method == "POST":
        d_schedule= SessionAttendance.objects.get(id=child_id)
        d_schedule.delete()
        return redirect('/')
    dele = SessionAttendance.objects.get(id=child_id)
    dele.delete()
    messages.success(request, 'Session Log Has Successfully Been Deleted!')
    return render(request, 'caseload/sessions.html')  


def new_session_log(request):
    form = NewSessionLog()
    if request.method == "POST":
        form = NewSessionLog(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Session Log Has Successfully Been Added!')
            return render(request, 'caseload/sessions.html')
    return render(request, 'caseload/new_session_log.html', {'form': form}) 


