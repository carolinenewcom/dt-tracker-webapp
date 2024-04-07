from django.urls import path
from . import views


urlpatterns = [
    path('', views.caseload),
    path('schedule/', views.schedule),
    path('sessions/', views.sessions),
    path('attendance/', views.attendance),

]