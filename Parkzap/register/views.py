
from django.shortcuts import render, redirect,HttpResponse
from .models import User
from django.core.mail import send_mail
from django.contrib.auth import settings
from datetime import datetime,timedelta



def signup(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        password=request.POST['password']
        dob=dob.split('/')
        dob=[int(i) for i in dob]
        dob_year_date_swap=dob[0]
        dob[0]=dob[1]
        dob[1]=dob_year_date_swap
        dob.reverse()
        dob=datetime(*dob).strftime("%Y-%m-%d")

        if (User.objects.filter(email=email).exists()):
            return HttpResponse("user already exists")
        else:
          user=User(name=name,date_of_birth=dob,email=email,password=password)
          send_mail("Registration", "Here is thanks for registering " + name, settings.EMAIL_HOST_USER, [email],
                          fail_silently=False)

          user.save()
          return redirect('status')


    else:
        return render(request,'signup.html',{'maxdate':(datetime.now() - timedelta(days=18*365)).strftime("%Y-%m-%d")})

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if(User.objects.filter(email=email,password=password).exists()):
          return redirect('status')
        else:
            return render(request, 'login.html' ,{'error_password':True})
    else:
        return render(request,'login.html')

def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
def status(request)  :
    if request.method == 'GET':
        return render(request, 'status.html')
