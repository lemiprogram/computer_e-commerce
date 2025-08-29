
from django.urls import path
from .views import *
urlpatterns = [
    path('get_Categories/all', get_Categories,name='get_Categories'),
    path('get_Conditions/all', get_Conditions,name='get_Conditions'),
    path('get_Stores/all', get_Stores,name='get_Stores'),
    path('get_Shoppers/all', get_Shoppers,name='get_Shoppers'),
    path('get_Sellers/all', get_Sellers,name='get_Sellers'),
    path('get_Products/all', get_Products,name='get_Products'),
    path('get_Orders/all', get_Orders,name='get_Orders'),
    path('get_Carts/all', get_Carts,name='get_Carts'),
    path('get_CartItems/all', get_CartItems,name='get_CartItems'),
    path('get_Wishlists/all', get_Wishlists,name='get_Wishlists'),
]
