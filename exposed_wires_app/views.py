
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .decorators import *
@redirect_admin             
def home(request):
    return render(request, 'index.html')

def shop(request):
    context = {
        'products':Product.objects.all()
    }
    if request.user.is_authenticated:
        if hasattr(request.user, "shopper_profile"):
            context["role"] = "shopper"
        elif hasattr(request.user, "seller_profile"):
            context["role"] = "seller"
    else:
        context["role"] = "user"
    return render(request, "shoppers/shop.html", context)
def view_products(request):
    page_number = request.GET.get('page','1')
    query  = request.GET.get('p','')
    products = Product.objects.filter(name__icontains=query)
    return render()
def account(request):
    context = {
        'user' : request.user,
    }
    if context['user'].is_authenticated:
        
        return render(request,'account.html', context)
    return redirect('sign_in')

def category_list(request):
    categories = Category.objects.all()
    return render(request, "shoppers/category_list.html", {"categories": categories})

def category_detail(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, "shoppers/category_detail.html", {
        "category": category,
        "products": products
    })
def wishlist(request):
    return render(request, 'shoppers/wishlist.html')
def deals(request):
    return render(request, "shoppers/deals.html")
#seller section
def seller_dashboard(request):
    return render(request, 'sellers/dashboard.html')
def add_product(request):
    return render(request, "sellers/add_product.html")

def manage_products(request):
    context = {
        'form':ProductForm()
    }
    return render(request, "sellers/manage_products.html",context)

def manage_orders(request):
    return render(request, "sellers/manage_orders.html")
def reports(request):
    return render(request, 'sellers/reports.html')
def seller_account(request):
    return render(request, "sellers/account.html")