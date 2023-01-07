from .models import CustomUser, UserShift
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import authenticate, login
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializers import CustomeRegisterSerializer, CustomerUserDetailSerializer, UserSerializer, UserShiftSerializer, UserShiftListSerializer

# Create your views here.
class UserRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomeRegisterSerializer

class UserListView(ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'status': 'success'})
        else:
            return Response({'status': 'User Not Found'})

class UserShiftViewSet(CreateModelMixin, GenericViewSet):
    queryset = UserShift.objects.all()
    serializer_class= UserShiftSerializer

class UserShiftListView(ListModelMixin, GenericViewSet):
    queryset = UserShift.objects.all()
    serializer_class = UserShiftListSerializer


class UserShiftDetailListView(ListModelMixin, GenericViewSet):
    serializer_class = CustomerUserDetailSerializer

    def get_queryset(self):
        # import pdb; pdb.set_trace()
        user_id = self.kwargs.get('user_id', None)
        if user_id is not None:
            return UserShift.objects.filter(user__id=user_id)
        return UserShift.objects.all()
