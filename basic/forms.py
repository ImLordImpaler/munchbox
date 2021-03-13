from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import BillingAddress
from django.forms import ModelForm

class NewCheckOut(ModelForm):
    class Meta:
        model    = BillingAddress
        fields = "__all__"

class NewUser(UserCreationForm):
    class Meta:
        model=User
        fields = ['username'  ]