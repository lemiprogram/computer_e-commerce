
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from registration.models import CustomUser
from .models import *
from .decorators import *
from django.contrib import messages
@redirect_admin             
def home(request):
    return render(request, 'index.html')

def shop(request):
    context = {
        'product':Product.objects.get(pk=7)
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
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller_profile
            product.save()
            messages.success(request, "Product added successfully!")
            return redirect("manage_products")  
    else:
        form = ProductForm()

    return render(request, "sellers/add_product.html", {"form": form})
def manage_products(request):
    

    user = request.user 
    seller = Seller.objects.get(user=user)
    products = Product.objects.filter(seller=seller)
    context = {
        'products':products
    }
    return render(request, "sellers/manage_products.html",context)

def manage_orders(request):
    return render(request, "sellers/manage_orders.html")
def reports(request):
    return render(request, 'sellers/reports.html')
def seller_account(request):
    return render(request, "sellers/account.html")
def stores(request):
    # Check if user is a seller with a store
    seller = getattr(request.user, "seller", None)
    store = seller.store if seller and hasattr(seller, "store") else None

    return render(request, "sellers/stores.html", {"store": store})


def create_store(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        city = request.POST.get("city")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        website = request.POST.get("website")

        if not name:
            messages.error(request, "Store name is required.")
            return redirect("create_store")

        # Create new store
        store = Store.objects.create(
            name=name,
            description=description,
            city=city,
            address=address,
            phone=phone,
            website=website,
        )

        # Link store to seller
        seller, _ = Seller.objects.get_or_create(user=request.user)
        seller.store = store
        seller.save()

        messages.success(request, f"Store '{store.name}' created successfully!")
        return redirect("stores")

    return render(request, "create_store.html")


def join_store(request):
    if request.method == "POST":
        store_id = request.POST.get("store_id")
        store = get_object_or_404(Store, id=store_id)

        seller, _ = Seller.objects.get_or_create(user=request.user)
        seller.store = store
        seller.save()

        messages.success(request, f"You have joined '{store.name}' successfully!")
        return redirect("stores")

    stores = Store.objects.all()
    return render(request, "join_store.html", {"stores": stores})