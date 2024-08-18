from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib.auth import logout as log
# Create your views here.
def index(request):
    return render(request,'index.html')

from django.shortcuts import redirect

def logout(request):
    log(request)
    return redirect('login') 

def loginn(request):
    if request.method=="POST":
        name=request.POST['name']
        print(name)
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        #login funtion sets the session variables necessary fo rmaintaininge 
        #requeried sesstions
        if user is not None:
            login(request,user)
            context={'userdetails':user}
            return render(request,'home.html',context)
        else :
            return redirect('signup')

    return render(request,'login.html')
def signup(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        #above code is saved
        return redirect('login')

    return render(request,'signup.html')

