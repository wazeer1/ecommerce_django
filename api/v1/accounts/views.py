from accounts.models import Profile
from api.v1.accounts.serializers import LoginSerializer, MinimalSerializer, RegisterSerializer
from api.v1.main.functions import generate_serializer_errors
from cart.models import Cart
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from main.encryption import decrypt,encrypt
from django.contrib.auth.models import Group, User
import requests
from rest_framework.response import Response
from rest_framework import status




@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        username = request.data['username']
        password = request.data['password']
        fullname = request.data['fullname']
        phone = request.data['phone']
        print(username,password,fullname,phone)
        if Profile.objects.filter(phone = phone , email = phone,username = username).exists():
            response_data={
                'StatusCode':6001,
                'data':{
                    'title':'message',
                    'message':'already have account'
                }
            }
        else:
            user = User.objects.create_user(
                username = username,
                password = password
            )
            encpass = encrypt(password)
            if phone.isdigit():
                profile = Profile.objects.create(
                    user = user,
                    name = fullname,
                    username = username,
                    password = encpass,
                    phone = phone,
                )
                print(encpass)
            else:
                profile = Profile.objects.create(
                    user = user,
                    name = fullname,
                    password = encpass,
                    email = phone,
                )
            protocol = "http://"
            web_host = request.get_host()
            request_url = protocol + web_host + "/api/v1/accounts/token/"
            response = requests.post(
                        request_url, 
                        data={
                            'username': username,
                            'password': password,
                        },
                    )
            cart = Cart.objects.create(
                user= profile,
                name=username
            )
            response = response.json()
            response_data={
                'StatusCode':6000,
                'data':{
                    'title':'success',
                    'access': response,  
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        phone = request.data['phone']
        password = request.data['password']
        if phone.isdigit():
            if Profile.objects.filter(phone=phone).exists():
                profile=Profile.objects.get(phone=phone)
                decrpass=decrypt(profile.password)
                if password == decrpass:
                    protocol = "http://"
                    web_host = request.get_host()
                    request_url = protocol + web_host + "/api/v1/accounts/token/"
                    response = requests.post(
                        request_url, 
                        data={
                            'username': profile.username,
                            'password': password,
                        },
                    )
                    response = response.json()
                    response_data = {
                        "StatusCode": 6000,
                        "data": {
                            "title": "success",
                            "acess": response
                        }
                    }
                else:
                    response_data = {
                        "StatusCode": 6001,
                        "data": {
                            "title": "failed",
                            "message": 'incorrect password'
                        }
                    }
            else:
                response_data = {
                        "StatusCode": 6001,
                        "data": {
                            "title": "failed",
                            "message": 'no profile found on this number'
                        }
                    }
        else:
            if Profile.objects.filter(email=phone).exists():
                profile=Profile.objects.get(email=phone)
                decrpass=decrypt(profile.password)
                if password == decrpass:
                    protocol = "http://"
                    web_host = request.get_host()
                    request_url = protocol + web_host + "/api/v1/accounts/token/"
                    response = requests.post(
                        request_url, 
                        data={
                            'username': profile.username,
                            'password': password,
                        },
                    )
                    response = response.json()
                    response_data = {
                        "StatusCode": 6000,
                        "data": {
                            "title": "success",
                            "acess": response
                        }
                    }
                else:
                    response_data = {
                        "StatusCode": 6001,
                        "data": {
                            "title": "failed",
                            "message": 'incorrect password'
                        }
                    }
            else:
                response_data = {
                        "StatusCode": 6001,
                        "data": {
                            "title": "failed",
                            "message": 'no profile found on this mail'
                        }
                    }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serializer._errors)
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
def minimals(request):
    if Profile.objects.filter(user = request.user).exists():
        instance = Profile.objects.get(user = request.user)
        serialized = MinimalSerializer(
            instance,
            # many=True,
            context = {
                "request":request
            }
        ).data
        response_data={
            'StatusCode':6000,
            'data':{
                'title':'success',
                'data':serialized
            }
        }
    else:
        response_data={
            'StatusCode':6001,
            'data':{
                'title':'failed',
                'data':'no account not found'
            }
        }
    return Response(response_data,status=status.HTTP_200_OK)