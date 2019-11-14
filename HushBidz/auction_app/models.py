from django.db import models

class User(models.Model):
    thing = 0

# Create your models here.
class Auction(models.Model):
    name = models.CharField(max_length=256)
    auction_type = models.BooleanField()
    description = models.TextField(max_length=256)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
    start_time=models.DateTimeField('start_time')
    end_time=models.DateTimeField('end_time')
    numUsers = 0
#    auction_url=

    def __str__(self):
        return f"({self.id}) {self.name} {self.description}"

class Items(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=256)  
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=256)
    image = models.ImageField(upload_to='item_image')

    def __str__(self):
        return '(' + str(self.auction.id) + ') ' + self.description
