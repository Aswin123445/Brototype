from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request,'landing.html')
def login(request):
    return render(request,"login.html")
def signup(request):
    return render(request,"signup.html")
