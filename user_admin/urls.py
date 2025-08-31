from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/", admin_dashboard, name="admin_dashboard"),

    path("categories/", admin_category_list, name="admin_category_list"),
    path("categories/create/", admin_category_create, name="admin_category_create"),
    path("categories/delete/<int:pk>", admin_category_delete, name="admin_category_delete"),
    path("conditions/", admin_condition_list, name="admin_condition_list"),
    path("conditions/create/", admin_condition_create, name="admin_condition_create"),
    path("conditions/delete/<int:pk>", admin_category_delete, name="admin_condition_delete"),
    path("filters/", admin_filter_list, name="admin_filter_list"),
    path("filters/assign/<int:category_id>/<int:filter_id>/", assign_filter, name="assign_filter"),
    path("filters/create/", admin_create_filter, name="admin_create_filter"),


    path("sellers/", admin_seller_list, name="admin_seller_list"),
    path("shoppers/", admin_shopper_list, name="admin_shopper_list"),
    path("stores/", admin_store_list, name="admin_store_list"),

    path("settings/", settings, name="settings"),
    path("logout/", logout_view, name="logout"),
]
