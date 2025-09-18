from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .decorators import admin_required
from .forms import CategoryForm, ConditionForm
from exposed_wires_app.models import *
from django.shortcuts import get_object_or_404

@login_required
@admin_required
def admin_dashboard(request):
    context = {
        'sellers_count':Seller.objects.count(),
        'shoppers_count':Shopper.objects.count(),
        'stores_count':Store.objects.count(),
    }
    return render(request, "dashboard.html",context)

@login_required
@admin_required
def admin_category_list(request):
    context = {
        'categories':Category.objects.all()
    }
    return render(request, "category_list.html",context)

@login_required
@admin_required
def admin_condition_list(request):
    context = {
        'conditions':Condition.objects.all()
    }
    return render(request, "condition_list.html",context)

@login_required
@admin_required
def admin_seller_list(request):
    context = {
        'sellers': Seller.objects.all()
    }
    return render(request, "seller_list.html",context)

@login_required
@admin_required
def admin_shopper_list(request):
    context = {
        'shoppers': Shopper.objects.all()
    }
    return render(request, "shopper_list.html",context)

@login_required
@admin_required
def admin_store_list(request):
    return render(request, "store_list.html")

@login_required
@admin_required
def settings(request):
    return render(request, "settings.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

def admin_category_create(request):
    form = CategoryForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    return redirect('admin_category_list')
def admin_condition_create(request):
    form = ConditionForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('admin_condition_list')
    
def admin_category_delete(request,pk):
    to_delete = Category.objects.get(pk=pk)
    to_delete.delete()
    return redirect('admin_category_list')
def admin_condition_delete(request, pk):
    to_delete = Condition.objects.get(pk=pk)
    to_delete.delete()
    return redirect('admin_condition_list')
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

@login_required
@admin_required
def admin_filter_list(request):
    categories = Category.objects.prefetch_related("filters").all()
    filters = Filter.objects.all()

    return render(request, "filter_list.html", {
        "categories": categories,
        "filters": filters
    })


@admin_required
def assign_filter(request, category_id, filter_id):
    category = get_object_or_404(Category, id=category_id)
    filter_obj = get_object_or_404(Filter, id=filter_id)

    if filter_obj not in category.filters.all():
        category.filters.add(filter_obj)
    else:
        category.filters.remove(filter_obj)

    return redirect("admin_filter_list")


@admin_required
def admin_create_filter(request):
    key = request.POST.get("key")
    if key:
        Filter.objects.get_or_create(key=key.strip())
    return redirect("admin_filter_list")


@admin_required
def admin_store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    products = Product.objects.filter(seller__store=store)
    staff = Seller.objects.filter(store=store)

    context = {
        "store": store,
        "products": products,
        "staff": staff,
    }
    return render(request, "store_detail.html", context)