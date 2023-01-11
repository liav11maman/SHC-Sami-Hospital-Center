from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

 #--------------Site Urls-------------- 
urlpatterns = [
    #--------------Home urls-------------- 
    path('',views.home, name="home"),
    #--------------Login and Logout urls-------------- 
    path('signup/', views.signup, name="signup"),
    path('signup2/', views.signup2, name="signup2"),
    path('signin/', views.signin, name="signin"),
    path('signin2/', views.signin2, name="signin2"),
    path('signout/', views.signout, name="signout"),
    #--------------Patient urls-------------- 
    path('patient_panel/', views.patient_panel, name="patient_panel"),
    path('pharmacy/', views.pharmacy, name="pharmacy"),
    path('blood_donation/', views.blood_donation, name="blood_donation"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('medical_info/',views.medical_info,name="medical_info"),
    path('cardiology/',views.cardiology,name="cardiology"),
    path('pediatrics/',views.pediatrics,name="pediatrics"),
    path('maternity_department/',views.maternity_department,name="maternity_department"),
    path('kidney_transplant/',views.kidney_transplant,name="kidney_transplant"),
    path('neurology/',views.neurology,name="neurology"),
    path('cancer_medicine/',views.cancer_medicine,name="cancer_medicine"),
    path('urology_department/',views.urology_department,name="urology_department"),
    path('ophthalmology/',views.ophthalmology,name="ophthalmology"),
    path('orthopedics/',views.orthopedics,name="orthopedics"),
    path('thanks/',views.thanks,name="thanks"),
     #--------------Doctor urls-------------- 
    path('doctor_panel/', views.doctor_panel, name="doctor_panel"),
    path('patients_information/', views.show_patients_information, name="doctor_pat_info"),
    path('delete/<str:id>/', views.delete, name="delete"),
    path('upload/', views.upload, name="upload"),
    path('update_patient_info/<str:id>/', views.update_patient_info, name="update_patient_info"),
    path('doctor_of_the_month/', views.doctor_of_the_month, name="doctor_of_the_month"),
    #--------------Appointment urls-------------- 
    path('appointment/', views.appointment, name="appointment"),
    path('confirm_appointment/', views.confirm_appointment, name="confirm_appointment"),
    #-----------Live Chat urls-----------------
    path('live_chat_home/', views.live_chat_home, name='live_chat_home'),
    path('live_chat_home/<str:room>/', views.room, name='room'),
    path('live_chat_home/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
