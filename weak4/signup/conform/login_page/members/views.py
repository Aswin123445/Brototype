from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def home(request):
  template=loader.get_template('login.html')
  return HttpResponse(template.render())
def signup(request):
  template=loader.get_template('signup.html')
  return HttpResponse(template.render())