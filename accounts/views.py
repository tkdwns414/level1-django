from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from accounts.models import User
from rest_framework.exceptions import ValidationError,AuthenticationFailed
from django.contrib.auth import login as django_login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        raise AuthenticationFailed
    django_login(request=request, user=user)
    return Response({"msg":"login complete"})

@api_view(["POST"])
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    try:
        User.objects.create_user(username=username, password=password)
        return Response({"msg":"regist complete"})
    except:
        raise ValidationError("existing username")
    