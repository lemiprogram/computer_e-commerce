
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
    seller = Seller.objects.get(user=request.user)
    store = seller.store 
    staff_members = Seller.objects.filter(store=store)
    current_seller = Seller.objects.get(user=request.user)
    return render(request, "sellers/stores.html", {"store": store, 'staff':staff_members, "current_seller":current_seller})


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
        seller.store_role = 'admin'
        seller.save()

        messages.success(request, f"Store '{store.name}' created successfully!")
        return redirect("stores")

    return render(request, "sellers/create_store.html")


def join_store(request):
    if request.method == "POST":
        token = request.POST.get("access_token")
        try:
            store = Store.objects.get(access_token=token)
        except Store.DoesNotExist:
            messages.error(request, "Invalid store token. Please try again.")
            return redirect("join_store")

        # link seller to store (assuming request.user is seller)
        seller = Seller.objects.get(user=request.user)

        seller.store = store
        seller.store_role = 'staff  '
        seller.save()
        messages.success(request, f"You successfully joined {store.name}.")
        return redirect("stores")

    return render(request, "sellers/join_store.html")
def edit_store(request, pk):
    seller = Seller.objects.get(user=request.user)
    if seller.store_role != 'admin':
        return redirect('stores')
    store = get_object_or_404(Store, pk=pk)

    # Ensure the store belongs to this seller
    if seller.store != store:
        messages.error(request, "You can only edit your own store.")
        return redirect("stores")

    if request.method == "POST":
        store.name = request.POST.get("name")
        store.description = request.POST.get("description")
        store.city = request.POST.get("city")
        store.address = request.POST.get("address")
        store.phone = request.POST.get("phone")
        store.website = request.POST.get("website")

        if "profile_image" in request.FILES:
            store.profile_image = request.FILES["profile_image"]

        store.save()
        messages.success(request, f"Store '{store.name}' updated successfully!")
        return redirect("stores")

    # get all staff linked to this store
    staff_members = Seller.objects.filter(store=store)

    return render(request, "sellers/edit_store.html", {
        "store": store,
        "staff_members": staff_members
    })
