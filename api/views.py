
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
    'Customusers':[CustomUser,CustomUserSerializer],
}
def get_capital(str):
    first_letter_capitalized = str[0].upper()
    rest_of_string = str[1:]
    return first_letter_capitalized + rest_of_string
@api_view(['GET'])
def get_model(request,model,pk):
    my_model,my_serializer = MY_MODELS[get_capital(model)]
    all_models = my_model.objects.get(pk=pk) if pk else my_model.objects.all()

    serializer = my_serializer(all_models) if pk else my_serializer(all_models, many=True)
    return Response(serializer.data)
@api_view(['DELETE'])
def delete_model(request, model, pk):
    my_model, _ = MY_MODELS[get_capital(model)]

    try:
        instance = my_model.objects.get(pk=pk)
        instance.delete()
        return Response({"message": f"{get_capital(model)} with id {pk} deleted successfully."}, status=204)
    except my_model.DoesNotExist:
        return Response({"error": f"{get_capital(model)} with id {pk} not found."}, status=404)
@api_view(['POST'])
def post_model(request, model):
    my_model, my_serializer = MY_MODELS[get_capital(model)]

    serializer = my_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('posted successfully', status=204)
    return Response({"error":  "faild post"}, status=404)

@api_view(['PATCH'])
def patch_model(request, model,pk):
    my_model, my_serializer = MY_MODELS[get_capital(model)]
    instance = get_object_or_404(my_model, pk=pk)
    serializer = my_serializer(instance,data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response('posted successfully', status=204)
    return Response({"error":  "faild post"}, status=404)

@api_view(['GET'])
def get_user(request):
    if not request.user.is_authenticated:
        return Response({})
    serializer = CustomUserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
def get_model_by_page(request, model, page_amount):
    my_model, my_serializer = MY_MODELS[get_capital(model)]

    page_no = request.GET.get('page', 1)  # default to page 1
    paginator = Paginator(my_model.objects.all(), page_amount)

    try:
        page_results = paginator.page(page_no)
    except:
        return Response({
            "error": "Invalid page number"
        }, status=status.HTTP_400_BAD_REQUEST)

    serializer = my_serializer(page_results, many=True)

    return Response({
        "results_count": paginator.count,                
        "num_pages": paginator.num_pages,        
        "current_page": page_results.number,      
        "has_next": page_results.has_next(),      
        "has_previous": page_results.has_previous(),  
        "results": serializer.data               
    })
