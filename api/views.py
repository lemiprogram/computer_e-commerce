
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from exposed_wires_app.models import *
from .serializers import *

@api_view(['GET'])
def get_Categories(request):
    all_Category = Category.objects.all()
    serializer = CategorySerializer(all_Category, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Conditions(request):
    all_Condition = Condition.objects.all()
    serializer = ConditionSerializer(all_Condition, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Stores(request):
    all_Store = Store.objects.all()
    serializer = StoreSerializer(all_Store, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Shoppers(request):
    all_Shopper = Shopper.objects.all()
    serializer = ShopperSerializer(all_Shopper, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Sellers(request):
    all_Seller = Seller.objects.all()
    serializer = SellerSerializer(all_Seller, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Products(request):
    all_Product = Product.objects.all()
    serializer = ProductSerializer(all_Product, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Orders(request):
    all_Order = Order.objects.all()
    serializer = OrderSerializer(all_Order, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Carts(request):
    all_Cart = Cart.objects.all()
    serializer = CartSerializer(all_Cart, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_CartItems(request):
    all_CartItem = CartItem.objects.all()
    serializer = CartItemSerializer(all_CartItem, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_Wishlists(request):
    all_Wishlist = Wishlist.objects.all()
    serializer = WishlistSerializer(all_Wishlist, many=True)
    return Response(serializer.data)
