from django.urls import path
from . import views


urlpatterns = [
    path('', views.caseload),
    path('schedule/', views.schedule),
    path('sessions/', views.sessions),
    path('attendance/', views.attendance),
    path('login/', views.login, name='login'),
    path('search_caseload/', views.search_caseload, name='search-caseload'),

]