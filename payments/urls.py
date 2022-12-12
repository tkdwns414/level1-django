from django.urls import path, include
from rest_framework.routers import DefaultRouter
from payments.views import *

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('purchase/', purchase),
]