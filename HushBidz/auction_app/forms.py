from django import forms
from .models import Auction, Items




class AddAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('name', 'auction_type', 'description', 'start_time', 'end_time')



class AddItemForm(forms.ModelForm):
   class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'image')

