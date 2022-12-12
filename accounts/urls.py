from django.urls import path
from accounts.views import *

urlpatterns = [
    path('accounts/login', login),
    path('accounts/regist', register),
]