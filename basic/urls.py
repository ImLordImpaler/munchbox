from django.urls import path
from . import views
urlpatterns = [
    path('' , views.homepage , name='homepage'),
    path('menu' , views.menu , name='menu'),
    
    #categoryWise
    path('breakfast' , views.breakfast , name='breakfast'),
    path('lunch' , views.lunch , name='lunch'),
    path('dinner' , views.dinner , name='dinner'),
]