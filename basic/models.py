from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100 )

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=1000 )
    price = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    #image 
    desc = models.TextField(null=True , blank=True)
    pTime = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class OrderItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(Item , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def get_total(self):
        return self.item.price * self.quantity
    def __str__(self):
        return str(self.item.name + ' + ' + self.user.username)

class Order(models.Model):
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem )

    def get_final_price(self):
        total = 0
        for i in self.items.all():
            total = total + i.get_total()
        return total 

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User  , on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    p_address = models.TextField()
    t_address = models.TextField(null=True)
    #image

    def __str__(self):
        return str(self.f_name + ' ' + self.l_name)

class BillingAddress(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    street = models.CharField(max_length=1200  )
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10 )
    landmark = models.CharField(max_length=500 , null=True , blank=True)
    specialInstructions = models.TextField(null=True , blank=True)
    def __str__(self):
        return str(self.user + ' + ' + self.street)
    
    

    