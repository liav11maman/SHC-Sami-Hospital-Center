from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signin/signout', views.signout, name="backhome"),
    path('signout/', views.signout, name="signout"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('blood_donation/', views.blood_donation, name="blood_donation"),
    path('test/', views.test, name="test"),
]

'''
    path('signup/', views.signup_test, name="signup"),
    path('signin/', views.signin_test, name="signin"),
    path('signout/', views.signout_test, name="signout"),
   
    path('doctor_login/', views.loginDoctor, name="doctor_login"),
    path('doctor_login/doctor_signup', views.signup2, name="signup_doctor"),

    path('manager_login/', views.manager_login, name="manager_login"),
    
    path('patient_login/', views.signin_test, name="signin"),
    path('patient_login/patient_signup/', views.signup_test, name="signup"),
    path('signout/', views.signout_test, name="signout"),
 '''