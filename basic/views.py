from django.shortcuts import render , redirect
from .models import Item , Category , OrderItem , Order
from django.contrib.auth import login , logout , authenticate
from django.utils import timezone
from django.http import HttpResponse
from .forms import NewUser, NewCheckOut

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

#Three Course meal Start
#BreakFast

def breakfast(request):
    item1 = Item.objects.filter(category__name='BreakFast')
    itemCount = Item.objects.filter(category__name='BreakFast').count()

    popularItems = item1.filter(rating__gte = 3)
    
    params = {
        'item': item1 ,
        'count': itemCount,
        'popularItems' : popularItems
    }
    return render(request , 'basic/category/breakfast.html' , params)


#Lunch
def lunch(request):
    item1 = Item.objects.filter(category__name='Lunch')
    itemCount = item1.count()
    popularItems = item1.filter(rating__gte = 3)

    params = {
        'item' : item1,
        'count': itemCount,
        'popularItems' : popularItems
    }
    return render(request , 'basic/category/lunch.html' , params)



#dinner
def dinner(request):
    item1 = Item.objects.filter(category__name='Lunch')
    itemCount = item1.count()
    popularItems = item1.filter(rating__gte = 3)

    params = {
        'item' : item1,
        'count': itemCount,
        'popularItems' : popularItems
    }
    return render(request , 'basic/category/dinner.html', params)

#three course meal ends

def addToCart(request, pk):
    item = Item.objects.get(id=pk)
    orderItem,created = OrderItem.objects.get_or_create(
        item = item , 
        ordered=False, 
        user = request.user
    )
    order_qs= Order.objects.filter(user=request.user , ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk= item.pk).exists():
            orderItem.quantity = orderItem.quantity +1 
            orderItem.save()
            return HttpResponse('<h4>Quantity modified</h4>')
        else:
            order.items.add(orderItem)
            
            return HttpResponse('<h4>New Item Added</h4>')
            
    else:
        orderedDate = timezone.now()
        order = Order.objects.create(ordered_date=orderedDate , user= request.user )
        order.items.add(orderItem)
        return HttpResponse('<h4>New Order Created</h4>')


def recipt(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user = request.user , ordered=False).first()
        
    else:
        order = None
    params = {
        'order': order
    }
    return render(request , 'basic/recipt.html', params)

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request , username = uname , password = pwd )

        if user is not None:
            login(request , user)
            return redirect('menu')
        else:
            return redirect('breakfast')

    return render(request , 'basic/auth/login.html')

def logoutPage(request):
    logout(request)
    return redirect('homepage')

def createAccount(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return HttpResponse('something wrong')
    
    params = {
        'form':form
    }
    return render(request , 'basic/auth/createAccount.html' , params)

def profile(request):
    categories = Category.objects.all()
    
    orders = Order.objects.filter(user = request.user )
    
    

    params =  {
        'categories': categories
    }
    return render(request , 'basic/profile/profile.html' , params)

def checkout(request):
    form = NewCheckOut()
    if request.method == 'POST':
        form = NewCheckOut(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return HttpResponse('nai hua chutiye')
    params = {
        'form': form
    }
    return render(request , 'basic/checkout.html' , params)
    
            

