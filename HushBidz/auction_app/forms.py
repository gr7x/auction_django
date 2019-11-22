from django import forms
from .models import Auction, Items




class AddAuctionForm(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('name', 'description', 'start_time', 'end_time')
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'description': forms.TextInput(attrs={'required': True}),
            'start_time': forms.DateTimeInput(attrs={'required': True}),
            'end_time': forms.DateTimeInput(attrs={'required': True}),
        }


class AddItemForm(forms.ModelForm):
   class Meta:
        model = Items
        fields = ('name', 'price', 'description', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'price': forms.TextInput(attrs={'required': True}),
            'image': forms.FileInput(attrs={'required': False}),
        }

class PostForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ('highest_bidder', 'price')
        widgets = {
            'highest_bidder': forms.TextInput(attrs={'required': True}),
            'price': forms.TextInput(attrs={'required': True}),

        }