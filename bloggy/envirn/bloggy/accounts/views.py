from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignInForm

# Create your views here.

#signup page view 
def signup(request):
    if request.method == 'POST':
        print(request.POST['username'])
        form = SignInForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("helo")
            form.save()
            return redirect(signin)
        else:
            print(form.errors)
    else:

        form=SignInForm()
    context={'form':form}
    return render(request,'accounts/signup.html',context)

#signin page view
def signin(request):
    return render(request,'accounts/signin.html')

