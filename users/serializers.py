from .models import CustomUser
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    model = CustomUser
    fields = [
        'email', 'username', 'date_joined', 'last_login',
        'is_staff', 'department', 'position'
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
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = CustomUser
        fields = ('password', 'username', 'first_name', 'last_name',)
