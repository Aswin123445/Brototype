from django.urls import path
from . import views
urlpatterns=[
    path( 'signup/', views.signup , name = 'signup' ),
    path('signin/' , views.signin , name = 'signin' ),
    path('home_page/' , views.home_page , name = 'home_page')
]