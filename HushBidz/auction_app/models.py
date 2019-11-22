from django.db import models
from django.utils import timezone

class User(models.Model):
    thing = 0

def one_hour_hence():
    return timezone.now() + timezone.timedelta(hours=1)

# Create your models here.
class Auction(models.Model):
    name = models.CharField('name', max_length=256, default = 'Auction name')
    #auction_type = models.BooleanField('auction_type', default = False, null=True, blank=True )
    description = models.TextField('description', default = 'description', max_length=256)
    admin=models.CharField(max_length=256)
    start_time=models.DateTimeField('start_time', default = timezone.now)
    end_time=models.DateTimeField('end_time', default = one_hour_hence)
    numUsers = 0
#    auction_url=

    def __str__(self):
        return "({self.id}) {self.name} {self.description}"

class Items(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items')
    name = models.CharField('name', max_length=256, default='An Item')  
    price = models.DecimalField('price', max_digits=6, decimal_places=2, default='0.00')
    description = models.TextField('description', max_length=256, default='item description')
    image = models.ImageField('image', upload_to='item_image', null=True, blank=True)
    highest_bidder = models.CharField('bidder', max_length=256, default='no bids')  

    def __str__(self):
        return '(' + str(self.auction.id) + ') ' + self.description
