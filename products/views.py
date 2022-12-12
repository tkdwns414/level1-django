from django.shortcuts import render
from rest_framework import viewsets

from products.models import Product
from products.permissions import IsAdminOrReadOnly, ReadOnly
from products.serializers import *
from rest_framework.permissions import IsAdminUser

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser |  ReadOnly,)

# class CartViewSet(viewsets.ReadOnlyModelViewSet):
#     def get_queryset(self):
#         queryset = Cart.objects.filter(user = self.request.user)
#         return queryset
        
#     serializer_class = CartSerializer

# class ProductCartViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductCartSerializer
