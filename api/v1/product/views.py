from multiprocessing import context
from urllib import response
from django.db.models import Q

from jmespath import search
from accounts.models import Profile
from api.v1.accounts.serializers import LoginSerializer, MinimalSerializer, RegisterSerializer
from api.v1.main.functions import generate_serializer_errors
from api.v1.product.serializers import CategorySerializer, ProductsSerializer
from cart.models import Cart, CartProducts
from product.models import Category, Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from main.encryption import decrypt,encrypt
from django.contrib.auth.models import Group, User
import requests
from rest_framework.response import Response
from rest_framework import status



@api_view(['GET'])
@permission_classes((AllowAny,))
def products(request):
    search = request.GET.get('search')
    print(search)
    instance = Product.objects.filter(Q(name__icontains=search))
    serialized = ProductsSerializer(
        instance,
        many = True,
        context = {
            "request":request
        }
    ).data
    response_data = {
        "StatusCode":6000,
        'data':serialized
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def categories(request):
    instance = Category.objects.all()
    serialized = CategorySerializer(
        instance,
        many = True,
        context = {
            "request" : request
        }
    ).data
    response_data={
        "StatusCode":6000,
        "data":serialized
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_to_category(request,pk):
    user = request.user
    profile = Profile.objects.get(user = user)
    cart = Cart.objects.get(user = profile)
    if Product.objects.filter(pk = pk).exists():
        product = Product.objects.get(pk = pk)
        added_product = CartProducts.objects.create(
            cart = cart,
            product = product,
        )
    else:
        response_data={
            "StaatusCode":6001,
            "message":"no product found on this pk"
        }
    
    response_data = {
        "StatusCode":6000,
        "message":"success"
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def view_cart_product(request):
    profile = Profile.objects.get(user = request.user)
    cart = Cart.objects.get(user = profile)
    cart_products = CartProducts.objects.filter(cart = cart)
    instance = cart_products.product
    serialized = ProductsSerializer(
        instance,
        many = True,
        context = {
            'request':request
        }
    ).data
    response_data = {
        "StatusCode":6000,
        'data' :serialized
    }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes((AllowAny,))
def categorie_products(request,pk):
    category = Category.objects.get(pk=pk)
    instance = Product.objects.filter(category=category)
    serialized = ProductsSerializer(
        instance,
        context = {
            "request":request
        },
        many=True
    ).data
    response_data = {
        "StatusCode":6000,
        "data":serialized
    }
    return Response(response_data, status=status.HTTP_200_OK)