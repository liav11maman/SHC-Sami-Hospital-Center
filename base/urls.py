from django.urls import path, include
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
    path('upload/', views.upload, name="upload"),
    
    path('appointment/', views.appointment, name="appointment"),
    path('confirm_appointment/', views.confirm_appointment, name="confirm_appointment"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('delete/<str:id>/', views.delete_appointment, name="delete_appointment"),
    path('update_patient_info/<str:id>/', views.update_patient_info, name="update_patient_info"),
    path('update_patient_appointment/<str:id>/', views.update_patient_appointment, name="update_patient_appointment"),

    #-----------live chat-----------------
    path('live_chat_home/', views.live_chat_home, name='live_chat_home'),
    path('live_chat_home/<str:room>/', views.room, name='room'),
    path('live_chat_home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('live_chat_patient/', views.live_chat_patient, name='live_chat_patient'),
    path('live_chat_patient/<str:room>/', views.room, name='room2'),
    path('live_chat_patient/checkview', views.checkview, name='checkview2'),
    path('show_appointment_patient/', views.show_appointment_patient, name='show_appointment_patient'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
