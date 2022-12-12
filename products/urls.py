from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import *

# Create a router and register our viewsets with it.
product_router = DefaultRouter()
product_router.register('', ProductViewSet,basename="product")

cart_router = DefaultRouter()
# cart_router.register('', CartViewSet, basename="cart")
# cart_router.register('', ProductCartViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('product/', include(product_router.urls)),
    path('cart/', include(cart_router.urls))
]