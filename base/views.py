from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
=======
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
>>>>>>> GuyEzra


def home(request):
    return render(request, 'home.html')
  
def style(request):
    return render(request, 'style.css')

<<<<<<< HEAD
def manager_login(request):
    return render(request, 'manager_login.html')        

def loginPatient(request):
    page = 'login'
=======
'''
def manager_login(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'manager_login_signup.html',context)        

def loginPatient(request):
    page = 'login'
    form = UserCreationForm()
>>>>>>> GuyEzra
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user =User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

<<<<<<< HEAD
    context={'page':page}
=======
        user = authenticate(request, username=username, password=password)    

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')


    context={'page':page, 'form':form}
>>>>>>> GuyEzra
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
<<<<<<< HEAD
    page = 'signup'
    context = {}
    return render(request, 'patient_login_signup.html', context)
=======
    return render(request, 'signup.html')
>>>>>>> GuyEzra

def signup2(request):
    page = 'signup'
    context = {}
<<<<<<< HEAD
    return render(request, 'doctor_login_signup.html', context)    
=======
    return render(request, 'doctor_login_signup.html', context)    

def logout(request):
    logout(request)
    return redirect('home')
'''
'''----------------------------------test register-------------------------------------------'''

def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! ")
        
        return redirect('signin')
        
        
    return render(request, "signup.html")



def signin(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "index.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin.html")



def signout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('home')

def pharmacy(request):
    return render(request, 'pharmacy.html')

def blood_donation(request):
    return render(request, 'blood_donation.html')

        
    



        
>>>>>>> GuyEzra
