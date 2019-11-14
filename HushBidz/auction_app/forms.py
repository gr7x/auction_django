from django import forms
from .models import Auction, Items




class AddAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('name', 'auction_type', 'description', 'start_time', 'end_time')

'''
    name = forms.CharField(max_length=256)
    auction_type = forms.BooleanField()
    description = forms.CharField(max_length=256)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
    start_time=forms.DateTimeField()
    end_time=forms.DateTimeField()
    numUsers = 0
'''    

class AddItemForm(forms.ModelForm):
   class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'image')
'''
    name = forms.CharField(max_length=256)  
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.CharField(max_length=256)
    image = forms.ImageField()
'''
