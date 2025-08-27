
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from exposed_wires_app.models import Product, Shopper, Category
from .serializers import CartSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def cart_detail(request):
    shopper = get_object_or_404(Shopper, id=request.user.id)
    cart, created = Cart.objects.get_or_create(shopper=shopper)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_cart(request, product_id):
    shopper = get_object_or_404(Shopper, id=request.user.id)
    cart, _ = Cart.objects.get_or_create(shopper=shopper) # c
    product = get_object_or_404(Product, id=product_id)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, product_id):
    shopper = get_object_or_404(Shopper, id=request.user.id)
    cart = get_object_or_404(Cart, shopper=shopper)
    CartItem.objects.filter(cart=cart, product_id=product_id).delete()
    return Response({"detail": "Item removed from cart."}, status=status.HTTP_204_NO_CONTENT)
def get_categories(request):
    categories,_ = Category.objects.get_or_create()
    
    return categories