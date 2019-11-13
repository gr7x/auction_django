from django import forms




class AddAuctionForm(forms.Form):
    name = forms.CharField(max_length=256)
    auction_type = forms.BooleanField()
    description = forms.CharField(max_length=256)
   # admin=models.ForeignKey(Something... , on_delete=models.CASCADE)
    start_time=forms.DateTimeField()
    end_time=forms.DateTimeField()
    numUsers = 0
    


class AddItemForm(forms.Form):
    name = forms.CharField(max_length=256)  
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.CharField(max_length=256)

