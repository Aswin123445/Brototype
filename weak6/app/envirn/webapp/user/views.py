from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
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
       if user is not None :    
           if not user.is_staff:       
             request.session['username']=username
             user_login(request,user)
             messages.success(request,'user logged in sucessfully')
             return redirect(home)
           else :
             messages.error(request,'only users allowed here')
             return redirect(login)
       else :
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
             messages.success(request, "User created successfully.")
             return redirect(login)
        except IntegrityError:
             messages.error(request, "Username already exists.")
             return redirect(signup)

    return render(request,'signup.html')



#admin view model
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_login(request):
    if 'admin' in request.session:
        return redirect(admin_home)
    if request.method=='POST':
       username= request.POST['name']
       password=request.POST['password']
       user=authenticate(username=username,password=password)
       if user is not None:
           if user.is_staff:
              request.session['admin']=username
              user_login(request,user)
              messages.success(request,'admin logged in sucessfully')
              return redirect(admin_home)
           else:
             messages.error(request,'user not allowed here!')
       else:
           messages.error(request,'invalid username or password')
           return redirect(admin_login)
    return render(request,'login.html')
#fetching the data from the user
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_home(request):
    if 'admin' in request.session:
      all_users = User.objects.all()
      context = {'all_users': all_users}
      return render(request, 'admin_home.html', context)
    return redirect(admin_login)

#deleting user from the admin page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_user_delete(request, user_id):
        try:
          user = User.objects.get(id=user_id)
          user.delete() if  not user.is_staff else None
          return redirect(admin_home)  # Redirect to a success page
        except User.DoesNotExist:
          messages.error(request, "User does not exist.")
          return redirect('admin_home')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def admin_user_details(request,user_id):
    if 'admin' in request.session:
      user = get_object_or_404(User, id=user_id)
      context={'user':user,'id':user_id}
      print(request.session['admin'])
      return render(request,'admin_user_details.html',context)
    else:
       print('ahi')
       return redirect(admin_login)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_user(request,user_id):
    user = User.objects.get(id=user_id)
    user.username=request.POST['username']
    user.save()
    messages.success(request,'User Name created sucessfully ')
    return redirect(admin_home)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update_email(request,user_id):
    user = User.objects.get(id=user_id)
    user.email=request.POST['email']
    user.save()
    messages.success(request,'Email Updated sucessfully')
    return redirect(admin_home)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_user_from_admin(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        data=request.POST['is_dmin']
        try:
             if User.objects.filter(username=username).exists():
                 raise IntegrityError()
             if data == 'option2':
               myuser=User.objects.create_user(username,email,password)
               myuser.save()
               messages.success(request, "User created successfully.")
               return redirect(admin_home)
             else:
               myuser=User.objects.create_user(username,email,password)
               myuser.is_staff=True
               myuser.is_superuser=True
               myuser.save()
               messages.success(request, "Admin created successfully.")
               return redirect(admin_home)
        except IntegrityError:
             messages.error(request, "Username already exists.")
             return redirect(admin_home)

    return render(request,'signup.html')

#logout user

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def admin_logout(request):
    if 'admin' in request.session:
        user_logout(request)
        messages.success(request,'admin logout successfull')
        return redirect(admin_login)
    return redirect(admin_login)


