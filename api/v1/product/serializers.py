from rest_framework import serializers
from product.models import *



class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'offer',
            'offer_price',
            'category',
        )
    def get_category(self,instance):
        category = "hello"
        return category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')