from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from psycopg2 import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    if 'username' in request.session:#section valid checking
      user_logout(request)
      messages.success(request,"logout sucessfull")
      return redirect(login) 
    return redirect(login)

def start(request):
    return render(request,'landing.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method=='POST':
       username= request.POST['name']
       password=request.POST['password']
       user=authenticate(username=username,password=password)
       if user is not None:
           
           request.session['username']=username
           user_login(request,user)
           messages.success(request,'user logged in sucessfully')
           return redirect(home)
       else:
           messages.error(request,'invalid username or password')
           return redirect(login)
    return render(request,'login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method=="POST":
        username=request.POST["name"]
        password=request.POST["password"]
        email=request.POST["email"]
        try:
             if User.objects.filter(username=username).exists():
                 raise IntegrityError()
             myuser=User.objects.create_user(username,email,password)
             myuser.save()
             print('user created susessfully')
             messages.success(request, "User created successfully.")
             print(messages)
             return redirect(login)
        except IntegrityError:
             messages.error(request, "Username already exists.")
             return redirect(signup)

    return render(request,'signup.html')
