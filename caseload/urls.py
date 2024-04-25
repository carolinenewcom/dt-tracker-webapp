from django.urls import path
from . import views


urlpatterns = [
    path('', views.caseload),
    path('schedule/', views.schedule),
    path('sessions/', views.sessions),
    path('attendance/', views.attendance),
    path('login/', views.login, name='login'),
    path('search_caseload/', views.search_caseload, name='search-caseload'),
    path('new_child/', views.new_child, name='new-child'),
    path('delete_child/<child_id>', views.delete_child, name='delete-child'),
    path('new_schedule/', views.new_schedule, name='new-schedule'),
    path('delete_schedule/<child_id>', views.delete_schedule, name='delete-schedule'),
    path('attendance_report/', views.attendance_report, name='attendance-report'),
    path('new_session_log/', views.new_session_log, name='new-session-log'),
]