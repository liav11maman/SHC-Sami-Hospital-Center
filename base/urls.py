from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# import room.urls

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signup2/', views.signup2, name="signup2"),
    path('signin/', views.signin, name="signin"),
    path('signin2/', views.signin2, name="signin2"),
    path('signout/', views.signout, name="signout"),



    path('patient_panel/', views.patient_panel, name="patient_panel"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('blood_donation/', views.blood_donation, name="blood_donation"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('patient_appointments/', views.patient_appointments,
         name="patient_appointments"),
    path('patient_upload/', views.patient_upload, name="patient_upload"),
    path('patient_send_message/', views.patient_send_message,
         name="patient_send_message"),
    path('room/', views.room, name="room"),



    path('doctor_panel/', views.doctor_panel, name="doctor_panel"),
    path('patients_information/',
         views.show_patients_information, name="doctor_pat_info"),
    path('upload/', views.upload, name="upload"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
