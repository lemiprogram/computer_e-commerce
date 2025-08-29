
from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.models import CustomUser
from .models import *
from registration.forms import INPUT_CLASS

class ProductForm(forms.ModelForm):
    name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Product name",
            "class": INPUT_CLASS
        })
    )

    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={
            "placeholder": "Enter price",
            "class": INPUT_CLASS
        })
    )

    stock = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "Available stock",
            "class": INPUT_CLASS
        })
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": INPUT_CLASS})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": INPUT_CLASS})
    )

    condition = forms.ModelChoiceField(
        queryset=Condition.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": INPUT_CLASS})
    )

    brand = forms.CharField(
        max_length=200, 
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Brand",
            "class": INPUT_CLASS
        }))
    discount = forms.IntegerField(
        required=True,
        min_value=0,
        max_value=100,
        initial=0,
        widget=forms.NumberInput(attrs={
            "placeholder": "Discount (%)",
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = Product
        fields = [
            "name","image","price", "stock","discount","category", "condition", "brand", 
            
        ]