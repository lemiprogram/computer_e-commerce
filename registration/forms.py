
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from exposed_wires_app.models import *
from .models import *

from django import forms
from exposed_wires_app.models import Shopper, Seller

# Tailwind style class for inputs
INPUT_CLASS = "w-full p-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-primary-100"


class ShopperForm(forms.ModelForm):
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your phone number",
            "class": INPUT_CLASS
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter your address",
            "class": INPUT_CLASS,
            "rows": 3
        })
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your city",
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = Shopper
        fields = ["phone", "address", "city"]


class SellerForm(forms.ModelForm):
    store_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your store name",
            "class": INPUT_CLASS
        })
    )
    store_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Describe your store",
            "class": INPUT_CLASS,
            "rows": 3
        })
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your city",
            "class": INPUT_CLASS
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your phone number",
            "class": INPUT_CLASS
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter your address",
            "class": INPUT_CLASS,
            "rows": 3
        })
    )

    class Meta:
        model = Seller
        fields = ["store_name", "store_description", "city", "phone", "address"]

class SignUpForm(UserCreationForm):
    INPUT_CLASS = "w-full p-3 bg-bg-300 text-text-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-200"
    USER_TYPE_CHOICES = [
        ('shopper', 'Shopper'),
        ('seller', 'Seller'),
    ]

    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Username...",
            "class": INPUT_CLASS
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Email...",
            "class": INPUT_CLASS
        })
    )
    role = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.Select(attrs={
            'class': INPUT_CLASS
        }),
        initial=USER_TYPE_CHOICES[0],
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password...",
            "class": INPUT_CLASS
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm Password...",
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "role", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Assign role-specific models
        return user