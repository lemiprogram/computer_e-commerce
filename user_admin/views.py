from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .decorators import admin_required
from .forms import CategoryForm, ConditionForm
from exposed_wires_app.models import Category, Condition

@login_required
@admin_required
def admin_dashboard(request):
    return render(request, "dashboard.html")

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
    return render(request, "seller_list.html")

@login_required
@admin_required
def admin_shopper_list(request):
    return render(request, "shopper_list.html")

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
    form = CategoryForm(request.POST)
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
