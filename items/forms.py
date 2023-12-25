from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['ItemCode', 'ItemName', 'ItemDesc', 'Type', 'Make', 'category', 'price', 'unit']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['ItemCode', 'ItemName', 'ItemDesc', 'Type', 'Make', 'category', 'price', 'unit']
