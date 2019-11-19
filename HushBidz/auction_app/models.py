from django.db import models

class User(models.Model):
    thing = 0

# Create your models here.
class Auction(models.Model):
    name = models.CharField('name', max_length=256, null=True, blank=True)
    auction_type = models.BooleanField('auction_type', default = False, null=True, blank=True )
    description = models.TextField('description', default = 'description', max_length=256, null=True, blank=True)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
    start_time=models.DateTimeField('start_time', null=True, blank=True)
    end_time=models.DateTimeField('end_time', null=True, blank=True)
    numUsers = 0
#    auction_url=

    def __str__(self):
        return "({self.id}) {self.name} {self.description}"

class Items(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='items')
    name = models.CharField('name', max_length=256, default='An Item')  
    price = models.DecimalField('price', max_digits=6, decimal_places=2, default='00.00', null=True, blank=True)
    description = models.TextField('description', max_length=256, default='item description', null=True, blank=True)
    image = models.ImageField('image', upload_to='item_image', null=True, blank=True)

    def __str__(self):
        return '(' + str(self.auction.id) + ') ' + self.description
