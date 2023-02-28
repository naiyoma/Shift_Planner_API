from .models import CustomUser, UserShift, Organization
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializers import CustomeRegisterSerializer, CustomerUserDetailSerializer, UserSerializer, UserShiftSerializer, UserShiftListSerializer, OrganizationSerializer, LoginSerializer

# Create your views here.
class UserRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomeRegisterSerializer

class UserListView(ListModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserShiftViewSet(CreateModelMixin, GenericViewSet):
    queryset = UserShift.objects.all()
    serializer_class= UserShiftSerializer

class UserShiftListView(ListModelMixin, GenericViewSet):
    queryset = UserShift.objects.all()
    serializer_class = UserShiftListSerializer


class UserShiftDetailListView(ListModelMixin, GenericViewSet):
    serializer_class = CustomerUserDetailSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id', None)
        if user_id is not None:
            return UserShift.objects.filter(user__id=user_id)
        return UserShift.objects.all()


class OrganizationViewSet(CreateModelMixin, GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class= OrganizationSerializer