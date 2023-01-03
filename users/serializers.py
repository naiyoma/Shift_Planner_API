from .models import CustomUser
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email'
        ]
class CustomerUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'department')
        read_only_fields= ('email',)

class CustomeRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
            department=validated_data['department'],
            position=validated_data['position']
        )
        return user

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 
                'email', 'is_staff', 
                'department', 'position')
