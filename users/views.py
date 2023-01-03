from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework import generics
from .models import CustomUser
from .serializers import CustomeRegisterSerializer, CustomerUserDetailSerializer, UserSerializer

# Create your views here.

class UserRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomeRegisterSerializer

class UserListView(ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

  