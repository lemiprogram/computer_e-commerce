
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('view_products/',view_products, name='view_products'),
    path('account/', account, name='account'),
    path('wishlist/', wishlist, name='wishlist'),
    path('deals/', deals, name='deals'),
    path("products/<int:pk>/", product_detail_view, name="product_detail"),
    path("categories/", category_list, name="category_list"),
    path("categories/<str:category_name>/", category_detail, name="category_products"),
    path("checkout/", checkout, name="checkout"),
    path("place-order/", place_order, name="place_order"),


    path("seller/dashboard/", seller_dashboard, name="seller_dashboard"),
    path("seller/manage_products/", manage_products, name="manage_products"),
    path("seller/manage_products/add/", add_product, name="add_product"),
    path("seller/orders/", manage_orders, name="manage_orders"),
    path("seller/reports/", reports, name="reports"),
    path("seller/account/", seller_account, name="seller_account"),
    
    path("seller/stores/", stores, name="stores"),
    path("seller/stores/create/", create_store, name="create_store"),
    path("seller/stores/join/", join_store, name="join_store"),
    path("seller/stores/edit/<int:pk>", edit_store, name="edit_store"),
]
                        