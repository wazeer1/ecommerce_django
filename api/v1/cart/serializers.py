from pyexpat import model
from rest_framework import serializers
from cart.models import Cart, CartProducts



class CartViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'name',
        )
        