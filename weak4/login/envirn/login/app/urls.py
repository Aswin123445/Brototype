from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('',views.index,name='starting'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.loginn,name='login'),
    path("logout/", views.logout, name="logout"), 
    path('login/signup',views.signup,name='hai'),
   
]