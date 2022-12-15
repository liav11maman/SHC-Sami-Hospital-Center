from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signin2/', views.signin2, name="signin2"),
    path('signin/signout', views.signout, name="backhome"),
    path('signout/', views.signout, name="signout"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('blood_donation/', views.blood_donation, name="blood_donation"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('signin/patient_panel', views.patient_panel, name="patient_panel"),
    path('patient_panel', views.patient_panel, name="patient_panel2"),
    path('doctor_panel/', views.doctor_panel, name="doctor_panel"),
    path('doctor_panel/patients_information', views.show_patients_information, name="doctor_panel"),
    path('signin2/doctor_panel', views.doctor_panel, name="doctor_panel2"),
    path('doctor_panel/upload/', views.upload, name="upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
