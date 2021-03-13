from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name='homepage'),
    path('menu' , views.menu , name='menu'),
    
    #categoryWise
    path('breakfast' , views.breakfast , name='breakfast'),
    path('lunch' , views.lunch , name='lunch'),
    path('dinner' , views.dinner , name='dinner'),
    path('recipt' , views.recipt , name='recipt'),


    #  ADD TO CART
    path('addToCart/<str:pk>/', views.addToCart , name='addToCart' ),


    # Auth
    path('loginPage' , views.loginPage , name='loginPage'),
    path('logoutPage' , views.logoutPage , name='logoutPage'),
    path('createAccount' , views.createAccount , name='createAccount'),

    #Checkout
    path('checkout'  , views.checkout , name='checkout'),
    #profile
    path('profile', views.profile , name='profile')


]