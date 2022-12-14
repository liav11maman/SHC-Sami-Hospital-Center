from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, Appointment
from django.core.files.storage import FileSystemStorage
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .forms import EditPatientForm
from .models import ContactUs
from .models import BloodDon


def home(request):
    return render(request, 'index.html')

    
def patients_information(request):
    return render(request, 'patients_information.html')
  
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


# @login_required(login_url='signin')
def pharmacy(request):
    return render(request, 'pharmacy.html')

# @login_required(login_url='signin')
def blood_donation(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        blood_type=request.POST['blood_type']

        new_blood_don=BloodDon(first_name=first_name,last_name=last_name,email=email,address=address,phone=phone,blood_type=blood_type)
        new_blood_don.save()
        return render(request, 'thanks.html')

    return render(request, 'blood_donation.html')

# @login_required(login_url='signin')
def aboutus(request):
    if request.method == "POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        new_aboutUs=ContactUs(name=name,phone=phone,email=email,subject=subject,message=message)
        new_aboutUs.save()
        return render(request, 'thanks.html')

    return render(request, 'aboutus.html')

@login_required(login_url='signin')    
def patient_panel(request):
    return render(request, 'patient_panel.html')

@login_required(login_url='signin2')
def doctor_panel(request):
    dc = Doctor.objects.all()
    return render(request, 'doctor_panel.html', {'dc':dc})

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

@login_required(login_url='signin2')
def delete(request, id):
    data = get_object_or_404(Patient, id=id) 
    data.delete()
    return redirect('doctor_pat_info')
 
def update_patient_info(request, id):
    context ={}
    obj = get_object_or_404(Patient, id = id)
    form = EditPatientForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/patients_information')
 
    context["form"] = form
 
    return render(request, "update_patient_info.html", context)


def doctor_of_the_month(request):
    return render(request, 'doctor_of_the_month.html')

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

def thanks(request):
    return render(request, 'thanks.html')


#---------------------------------------------------------------------------
def appointment(request):

    if request.method == 'POST':

        your_fname = request.POST.get('your_fname')
        your_lname= request.POST.get('your_lname')
        your_email = request.POST.get('your_email')
        your_phone = request.POST.get('your_phone')
        your_date = request.POST.get('your_date')
        your_time = request.POST.get('your_time')
        your_description = request.POST.get('your_description')

        context = {
            'your_fname' : your_fname,
            'your_lname' : your_lname,
            'your_email' : your_email,
            'your_phone' : your_phone,
            'your_date' : your_date,
            'your_time' : your_time,
            'your_description' : your_description,
        }

        my_appointment = Appointment.objects.create(patient_first_name = your_fname, patient_last_name = your_lname, patient_email = your_email,
        patient_phone_number = your_phone, appointment_date = your_date, appointment_time = your_time, description = your_description)
        
        my_appointment.save()
        
        return render(request, 'confirm_appointment.html', context)


    return render(request, 'appointment.html')    

        

def confirm_appointment(request):
    return render(request, 'confirm_appointment.html')        

@login_required(login_url='signin2')
def delete(request, id):
    data = get_object_or_404(Patient, id=id) 
    data.delete()
    return redirect('doctor_pat_info')

def test(request):
    return render(request, 'test.html')
 
def update_patient_info(request, id):
    context ={}
    obj = get_object_or_404(Patient, id = id)
    form = EditPatientForm(request.POST or None, instance = obj)
 
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/patients_information')
 
    context["form"] = form
 
    return render(request, "update_patient_info.html", context)

#--------------------live chat------------------------------
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def live_chat_home(request):
    return render(request, 'live_chat_home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})