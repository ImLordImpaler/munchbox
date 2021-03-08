from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request , 'basic/index.html')

def menu(request):
    return render(request , 'basic/menu.html')