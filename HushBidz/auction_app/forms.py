from django import forms
from .models import Auction, Items




class AddAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('name', 'description', 'start_time', 'end_time')



class AddItemForm(forms.ModelForm):
   class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'image')

class PostForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('highest_bidder', 'price')