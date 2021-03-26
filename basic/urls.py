from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage , name='homepage'),
    path('menu' , views.menu , name='menu'),
    path('item/<str:pk>/' , views.item , name='item'),
    #categoryWise
    
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
    path('profile', views.profile , name='profile'),
    path('category/<str:pk>/' , views.category , name='category'), 

    path('becomePartner' , views.becomePartner, name="becomePartner"),


    #admin 
    path('adminPage' , views.adminPage , name='adminPage')


]