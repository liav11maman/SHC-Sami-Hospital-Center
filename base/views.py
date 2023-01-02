from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Patient
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView



def home(request):
    return render(request, 'index.html')
  
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

def signup2(request):
    
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
        
        return redirect('signin2')
        
        
    return render(request, "signup2.html")




def signin(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "patient_panel.html",{"fname":fname})
            return redirect('patient_panel')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin.html")


def signin2(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "patient_panel.html",{"fname":fname})
            return redirect('doctor_panel')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    
    return render(request, "signin2.html")



def signout(request):
    logout(request)
    messages.success(request, 'logged out')
    return redirect('home')


@login_required(login_url='signin')
def pharmacy(request):
    return render(request, 'pharmacy.html')

@login_required(login_url='signin')
def blood_donation(request):
    return render(request, 'blood_donation.html')

@login_required(login_url='signin')
def aboutus(request):
    return render(request, 'aboutus.html')

@login_required(login_url='signin')    
def patient_panel(request):
    return render(request, 'patient_panel.html')

@login_required(login_url='signin2')
def doctor_panel(request):
    return render(request, 'doctor_panel.html')

@login_required(login_url='signin2')
def show_patients_information(request):
    pt = Patient.objects.all()
    return render(request, 'patients_information.html', {'pt':pt})


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

def test(request):
    return render(request, 'test.html')

def medical_info(request):
    return render(request, 'medical_info.html')

def cardiology(request):
    return render(request, 'cardiology.html')

def pediatrics(request):
    return render(request, 'pediatrics.html')

def maternity_department(request):
    return render(request, 'maternity_department.html')

def kidney_transplant(request):
    return render(request, 'kidney_transplant.html')

def neurology(request):
    return render(request, 'neurology.html')

def cancer_medicine(request):
    return render(request, 'cancer_medicine.html')

def urology_department(request):
    return render(request, 'urology_department.html')

def ophthalmology(request):
    return render(request, 'ophthalmology.html')

def orthopedics(request):
    return render(request, 'orthopedics.html')