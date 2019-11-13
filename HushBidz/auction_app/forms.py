from django import forms

class AddItemForm(forms.Form):
    name = forms.CharField(max_length=256)  
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    description = forms.TextField(max_length=256)
    image = forms.ImageField()