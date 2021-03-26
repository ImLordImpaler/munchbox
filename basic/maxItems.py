from .models import Item


def get_maximum_items(par):
    l1 = []
    item = Item.objects.filter(category__id =par ).order_by('-rating')
    for i in item:
        l1.append(i)
    return l1