from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home, name="home"),

   
    path('doctor_login/', views.loginDoctor, name="doctor_login"),
    path('doctor_login/doctor_signup', views.signup2, name="signup"),

    path('admin/', views.manager_login, name="manager_login"),
    
    path('patient_login/', views.loginPatient, name="patient_login"),
    path('patient_login/patient_signup/', views.signup, name="signup"),
    path('', views.style, name="style"),
]