from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from .models import User
from django.contrib.auth import authenticate, login


def loginn(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        print(email)
        password = request.POST.get('password')
        print(password)
        emaila=User.objects.get(email=email).email
        passs=User.objects.get(password=password).password
        if passs!=None and emaila!=None:
          pass
        print(emaila)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('home.html')  # Redirect to home page
        else:
            # Handle invalid login (show error message, etc.)
            print("helo")
            return redirect('signup')
    return render(request, 'login.html')  # Render login form
def home(request):
    template=loader.get_template("land.html")
    return HttpResponse(template.render())
def signup(request):
    if request.method=="POST":
        email=request.POST['mail']
        password=request.POST['password']
        myuser=User.objects.create(email=email,password=password)
        myuser.save()
        #above code is saved
        return redirect('loginn')

    return render(request,'signup.html')
