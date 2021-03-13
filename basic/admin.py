from django.contrib import admin

# Register your models here.
from .models import Item , Category , Order , OrderItem , Profile , BillingAddress
admin.site.register(BillingAddress)

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
admin.site.register(Category)