from django.forms import ModelForm, TextInput
from . models import AuctionListings
from django import forms

class AuctionListingsForm(ModelForm):
    class Meta:
        model = AuctionListings
        fields = ["item_name", "description", "url", "bid", "category"]
        widgets = {
            'item_name': TextInput(attrs={"class": "form-control", 'style': 'max-width: 900px;',
                'placeholder': 'Item Name'}),
            'description':TextInput(attrs={"class": "form-control", 'style': 'max-width: 900px;',
                'placeholder': 'Describe the item'}),
            'url': TextInput(attrs={"class": "form-control", 'style': 'max-width: 900px;',
                'placeholder': 'Paste your image url here'}),
            'bid': TextInput(attrs={"class": "form-control", 'style': 'max-width: 900px;',
                'placeholder': 'Enter Bid amount here'}),
            'category': TextInput(attrs={"class": "form-control", 'style': 'max-width: 900px;',
                'placeholder': 'Category Name'}),
        }