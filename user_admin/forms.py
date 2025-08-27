from django import forms
from exposed_wires_app.models import Seller, Store, Order,Category,Condition
from registration.forms import INPUT_CLASS


class SellerForm(forms.ModelForm):
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter city",
            "class": INPUT_CLASS
        })
    )
    phone = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter phone number",
            "class": INPUT_CLASS
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter address",
            "rows": 3,
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = Seller
        fields = ["store", "city", "phone", "address"]


class StoreForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter store name",
            "class": INPUT_CLASS
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter store description",
            "rows": 3,
            "class": INPUT_CLASS
        })
    )
    city = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter store city",
            "class": INPUT_CLASS
        })
    )
    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder": "Enter store address",
            "rows": 3,
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = Store
        fields = ["name", "description", "city", "address"]


class OrderForm(forms.ModelForm):
    status = forms.ChoiceField(
        choices=[
            ("pending", "Pending"),
            ("shipped", "Shipped"),
            ("delivered", "Delivered"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        widget=forms.Select(attrs={
            "class": INPUT_CLASS
        })
    )

    class Meta:
        model = Order
        fields = ["status"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['condition']