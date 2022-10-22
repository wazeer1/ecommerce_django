from accounts.models import Profile
from cart.models import Cart, CartProducts
from rest_framework import serializers
from urllib import request




class RegisterSerializer(serializers.Serializer):
    phone = serializers.CharField()
    fullname = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()


class MinimalSerializer(serializers.ModelSerializer):
    cart_dat = serializers.SerializerMethodField()
    class Meta:
        model = Profile
        fields = (
            'id',
            'name', 
            'phone',
            'email',
            'photo',
            'username',
            'dob', 
            'cart_dat',         
        )
    def get_cart_dat(self,instance):
        if Cart.objects.filter(user = instance).exists():
            cart = Cart.objects.get(user = instance)
            cart_dat = CartProducts.objects.filter(cart = cart).count()
        else:
            cart_dat=None
        return cart_dat

