from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as log
from django.views.decorators.cache import cache_control
from django.contrib import messages
# Create your views here.

#view funtion for landing page
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if 'username' in request.session:
        return redirect(home)
    return render(request,'index.html')
#view funtion for logout action 
def logout(request):
    if 'username' in request.session:#section valid checking
      log(request)
      return redirect(loginn) 
    return redirect(loginn)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginn(request):
    if 'username' in request.session:
       return redirect(home)
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        #authenticate funtion helps to check the username and password with database 
        user=authenticate(username=name,password=password)
        #login funtion sets the session variables necessary fo rmaintaininge 
        #requeried sesstions
        if user is not None:
            #setting session dictionary with key username and value name of the user
            request.session['username'] = name
            login(request,user)
            context={'userdetails':user}
            return redirect(home)
        else :
            messages.error(request,"Incorrect Password or Username")
            return redirect(loginn)
    return render(request,'login.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        #create user funtion will create a user in User model
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        #above code is saved
        return redirect('login')
    return render(request,'signup.html')
def hi(request):
    context={"name":"aswin"}
    return render(request,'helo.html',context)
