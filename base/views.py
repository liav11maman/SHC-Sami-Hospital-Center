from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')
  
def style(request):
    return render(request, 'style.css')

def manager_login(request):
    return render(request, 'manager_login.html')        

def loginPatient(request):
    page = 'login'
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user =User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

    context={'page':page}
    return render(request, 'patient_login_signup.html',context)

def loginDoctor(request):
    page = 'login'
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

    context={'page':page }
    return render(request, 'doctor_login_signup.html',context)


def signup(request):
    page = 'signup'
    context = {}
    return render(request, 'patient_login_signup.html', context)

def signup2(request):
    page = 'signup'
    context = {}
    return render(request, 'doctor_login_signup.html', context)    