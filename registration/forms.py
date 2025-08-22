
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from exposed_wires_app.models import *


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
            "placeholder": "Username",
            "class": INPUT_CLASS
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": INPUT_CLASS
        })
    )
    role = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        widget=forms.RadioSelect
        
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": INPUT_CLASS
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Confirm Password",
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
            if self.cleaned_data["role"] == "shopper":
                Shopper.objects.create(user=user)
            else:
                Seller.objects.create(user=user)
        return user