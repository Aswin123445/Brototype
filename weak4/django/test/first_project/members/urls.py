from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/data/<int:id>', views.details, name='details'),
    path("members/table/",views.tab,name='table'),
]
