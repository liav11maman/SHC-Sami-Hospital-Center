from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
  
def style(request):
    return render(request, 'style.css')

def patient_login(request):
    return render(request, 'patient_login.html')

def doctor_login(request):
    return render(request, 'doctor_login.html')

def manager_login(request):
    return render(request, 'manager_login.html')        


