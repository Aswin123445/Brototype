from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import SignUpForm,SignInForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate
import json

# Create your views here.

#signup page view 
@csrf_exempt
def signup(request):
    # data = json.loads(request.body)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("helo")
            form.save()
            return redirect(signin)
        else:
            print(form.errors)
    else:

        form=SignUpForm()
    context={'form':form}
    return render(request,'accounts/signup.html',context)

#signin page view
@csrf_exempt
def signin(request):
    form=None
    data=json.loads(request.body)
    if request.method == 'POST' :
        form=SignInForm(data)
        #form=SignInForm(request.POST)
        print(form)
        print(form.is_valid())
        print(form)
        if form.is_valid():
            user=authenticate(username = form.cleaned_data['email'], password = form.cleaned_data['password'])
            if user is not None :
                login(request , user)
                return redirect(home_page)
            else :
                print('form.errors')
                form.add_error(None , "invalid name or password")
        else :
            print(form.errors)
            form=SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

#home page view
@csrf_exempt
def home_page(requset):
    return render(requset,'accounts/home_page.html')
