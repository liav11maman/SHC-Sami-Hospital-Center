from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('patient_login/', views.patient_login, name="patient_login"),
    path('doctor_login/', views.doctor_login, name="doctor_login"),
    path('manager_login/', views.manager_login, name="manager_login"),

    path('', views.style, name="style"),
]