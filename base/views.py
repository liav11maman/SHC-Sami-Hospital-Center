from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, 'home.html')
  
def style(request):
    return render(request, 'style.css')

def doctor_login(request):
    return render(request, 'doctor_login.html')

def manager_login(request):
    return render(request, 'manager_login.html')        

def loginPatient(request):

    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user =User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

    context={}
    return render(request, 'patient_login.html',context)

def loginDoctor(request):

    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

    context={}
    return render(request, 'patient_login.html',context)
