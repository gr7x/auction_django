from django.db import models

# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length=256)    
    email    = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)




class Auction(models.Model):
    name = models.CharField(max_length=256)
    auction_type = models.BooleanField()
    description = models.TextField(max_length=256)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
    start_time=models.DateTimeField('start_time')
    end_time=models.DateTimeField('end_time')
#    auction_url=

class Items(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=256)  
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=256)
    
   # needs upload image added
