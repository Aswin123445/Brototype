from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as log
from django.views.decorators.cache import cache_control
from django.shortcuts import redirect
# Create your views here.
def index(request):
    if 'username' in request.session:
        return redirect(home)
    return render(request,'index.html')

def logout(request):
    if 'username' in request.session:
      log(request)
      return redirect(loginn) 
    return redirect('login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginn(request):
    if 'username' in request.session:
       return redirect(home)
    if request.method=="POST":
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(username=name,password=password)
        #login funtion sets the session variables necessary fo rmaintaininge 
        #requeried sesstions
        if user is not None:
            request.session['username'] = name
            login(request,user)
            context={'userdetails':user}
            return redirect(home)
        else :
            return redirect(signup)
    return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')
def signup(request):
    if 'username' in request.session:
        return redirect(home)
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        #above code is saved
        return redirect('login')
    return render(request,'signup.html')
    