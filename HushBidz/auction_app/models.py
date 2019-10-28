from django.db import models

# Create your models here.

class User(models.Model):
    fullName = models.CharField(max_length=256)    
    email    = models.EmailField(max_length=256)
    password = models.CharField(max_length=256)




#class Auction(models.Model):
#    name = models.CharField(max_length=50)
#    auction_type = models.BooleanField()
#    description = models.TextField(max_length=300)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
#    start_time=models.DateTimeField('start_time')
#    end_time=models.DateTimeField('end_time')
#    auction_url=
