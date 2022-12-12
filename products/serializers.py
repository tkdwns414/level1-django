from rest_framework import serializers
from products.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Cart
#         fields=["id", "products"]

# class ProductCartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=ProductCart
#         fields=["id", "amount"]
    