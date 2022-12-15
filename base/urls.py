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
    path('patients_information/', views.show_patients_information, name="patients_information"),
    path('test/', views.test, name="test"),
]