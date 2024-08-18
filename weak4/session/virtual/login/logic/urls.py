from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('loginn/',views.loginn,name='loginn'),
    path('signup/',views.signup,name='signup')
]