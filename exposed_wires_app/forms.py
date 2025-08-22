
from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.models import CustomUser
from .models import *

class SellerRegistrationForm(UserCreationForm):
    store_name = forms.CharField()
    store_description = forms.CharField(widget=forms.Textarea, required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        user.is_shopper = False
        if commit:
            user.save()
            # create profile
            Seller.objects.create(
                user=user,
                store_name=self.cleaned_data.get("store_name"),
                store_description=self.cleaned_data.get("store_description"),
                phone=self.cleaned_data.get("phone"),
                address=self.cleaned_data.get("address"),
            )
        return user
