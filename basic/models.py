from django.db import models

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
    pTime = models.IntegerField(default=0)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    