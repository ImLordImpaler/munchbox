from django.shortcuts import render
from .models import Item , Category
# Create your views here.

def homepage(request):
    return render(request , 'basic/index.html')

def menu(request):
    item1 = Item.objects.filter(category__name='BreakFast')
    item2 = Item.objects.filter(category__name='Lunch')
    item3 = Item.objects.filter(category__name='Dinner')

    category1 = Category.objects.get(name='BreakFast')
    category2 = Category.objects.get(name='Lunch')
    category3 = Category.objects.get(name='Dinner')

    
    params = {
        #filter items by category
        'breakfast': item1,
        'lunch': item2,
        'dinner': item3,
        'category1' : category1,
        'category2' : category2,
        'category3' : category3,



    }
    return render(request , 'basic/menu.html' , params)

def breakfast(request):
    item1 = Item.objects.filter(category__name='BreakFast')
    itemCount = Item.objects.filter(category__name='BreakFast').count()

    popularItems = Item.objects.filter(rating__gte=3.0)
    print(popularItems)
    params = {
        'item': item1 ,
        'count': itemCount
    }
    return render(request , 'basic/category/breakfast.html' , params)
def lunch(request):
    return render(request , 'basic/category/lunch.html')
def dinner(request):
    return render(request , 'basic/category/dinner.html')