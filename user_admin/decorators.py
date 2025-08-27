from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and getattr(request.user, "role", None) == "admin":
            return view_func(request, *args, **kwargs)
        return redirect('home')
    return wrapper