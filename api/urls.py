
from django.urls import path
from .views import *
urlpatterns = [
    path('get/<str:model>/<int:pk>', get_model,name='get_model'),
    path('get/user', get_user,name='get_user'),
    path('get_by_page/<str:model>/<int:page_amount>', get_model_by_page,name='get_model_by_page'),
]
