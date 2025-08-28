
# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import *
from exposed_wires_app.models import *
from .serializers import *

@api_view()
def get_products(request):
    data = {
        'name':'wayne',
        'age':20
    }
    return Response(data)


