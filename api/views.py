
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from exposed_wires_app.models import *
from .serializers import *
from django.core.paginator import Paginator
MY_MODELS = {
    'Categories':[Category,CategorySerializer],
    'Conditions':[Condition,ConditionSerializer],
    'Stores':[Store,StoreSerializer],
    'Shoppers':[Shopper,ShopperSerializer],
    'Sellers':[Seller,SellerSerializer],
    'Products':[Product,ProductSerializer],
    'Orders':[Order,OrderSerializer],
    'Carts':[Cart,CartSerializer],
    'CartItems':[CartItem,CartItemSerializer],
    'Wishlists':[Wishlist,WishlistSerializer],
}

@api_view(['GET'])
def get_model(request,model,pk):
    my_model,my_serializer = MY_MODELS[model.title()]
    all_models = my_model.objects.get(pk=pk) if pk else my_model.objects.all()

    serializer = my_serializer(all_models) if pk else my_serializer(all_models, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data )

@api_view(['GET'])
def get_model_by_page(request,model,page_amount):
    my_model,my_serializer = MY_MODELS[model.title()]
    page_no = request.GET.get('page')
    page_no = page_no if page_no else 1
    paginator = Paginator(my_model.objects.all(),page_amount)
    page_results = paginator.get_page(page_no)
    serializer = my_serializer(page_results, many=True)
    return Response(serializer.data)