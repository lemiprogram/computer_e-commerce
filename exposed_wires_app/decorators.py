from django.shortcuts import redirect
from functools import wraps

def redirect_admin(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", None) == "admin":
            return redirect("admin_dashboard")
        return view_func(request, *args, **kwargs)
    return wrapper
def redirect_shopper(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", None) == "shopper":
            return redirect("shop")
        return view_func(request, *args, **kwargs)
    return wrapper
def redirect_seller(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", None) == "seller":
            return redirect("seller_dashboard")
        return view_func(request, *args, **kwargs)
    return wrapper