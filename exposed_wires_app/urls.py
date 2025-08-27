
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('view_products/',view_products, name='view_products'),
    path('account/', account, name='account'),
    path('wishlist/', wishlist, name='wishlist'),
    path('deals/', deals, name='deals'),
    path("categories/", category_list, name="category_list"),
    path("categories/<str:category_name>/", category_detail, name="category_detail"),
    path("dashboard/", seller_dashboard, name="seller_dashboard"),
    path("manage_products/add/", add_product, name="add_product"),
    path("manage_products/", manage_products, name="manage_products"),
    path("orders/", manage_orders, name="manage_orders"),
    path("reports/", reports, name="reports"),
    path("seller/acccount/", seller_account, name="seller_account"),
]
                        