from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from .models import CustomUser
from .serializers import CustomeRegisterSerializer, CustomerUserDetailSerializer, UserSerializer

# Create your views here.

class UserRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomeRegisterSerializer
