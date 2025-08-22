
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('account/', account, name='account'),
    path("categories/", category_list, name="category_list"),
    path("categories/<str:category_name>/", category_detail, name="category_detail"),
]
                        