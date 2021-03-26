from django.shortcuts import render , redirect
from .models import Item , Category , OrderItem , Order
from django.contrib.auth import login , logout , authenticate
from django.utils import timezone
from django.http import HttpResponse
from .forms import NewUser, NewCheckOut
from .maxItems import get_maximum_items
def homepage(request):
    cat = Category.objects.all()
    
    params = {
        'cat':cat
    }
    return render(request , 'basic/index.html' , params)
def category(request ,pk):
    items = Item.objects.filter(category__id = pk)
    categoryName = items.first()
    itemsByRating = items.order_by('-rating')
    l1 = get_maximum_items(pk)
    if request.method == 'POST':
        minAmount = request.POST.get('minAmount')[1:]
        maxAmount = request.POST.get('maxAmount')[1:]
        items = Item.objects.filter(category__id=pk , price__gte = minAmount , price__lte= maxAmount)
        
    params ={
        'items' : items,
        'category' :categoryName,
        'itemsByRating':items,
        'topItems' : l1
    }
    return render(request , 'basic/category.html' , params)


def item(request , pk):
    item = Item.objects.get(id=pk)

    params = {
        'item':item
    }
    return render(request , 'basic/itemDetail.html' , params)
def menu(request):
    
    params = {
        #filter items by category
        
       



    }
    return render(request , 'basic/menu.html' , params)

#Three Course meal Start
#BreakFast


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
    return render(request , 'basic/cart.html', params)

def loginPage(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request , username = uname , password = pwd )

        if user is not None:
            login(request , user)
            return redirect('homepage')
        else:
            return redirect('cart')

    return render(request , 'basic/loginPage.html')

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


def becomePartner(request):
    return render(request , 'basic/becomePartner.html')


def adminPage(request):
    return render(request , 'basic/admin/dashboard.html')
    
            

