
from django.urls import path
from .views import *
urlpatterns = [
    path('products/get', get_products,name='get_products')
]
