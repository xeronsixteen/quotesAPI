from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.admin import User


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
