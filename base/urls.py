from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signup2/', views.signup2, name="signup2"),
    path('signin/', views.signin, name="signin"),
    path('signin2/', views.signin2, name="signin2"),
    path('signout/', views.signout, name="signout"),
    
    

    path('patient_panel/', views.patient_panel, name="patient_panel"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('blood_donation/', views.blood_donation, name="blood_donation"),
    path('aboutus/', views.aboutus, name="aboutus"),



    path('doctor_panel/', views.doctor_panel, name="doctor_panel"),
    path('patients_information/', views.show_patients_information, name="doctor_pat_info"),
    path('delete/<str:id>/', views.delete, name="delete"),
    # path('doctor_panel/', views.show_doctors_information, name="doctor_panel"),
    path('upload/', views.upload, name="upload"),
    path('update_patient_info/<str:id>/', views.update_patient_info, name="update_patient_info"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
