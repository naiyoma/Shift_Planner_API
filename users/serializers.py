from .models import CustomUser, UserShift, Organization
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'department', 'position', 'password'
        ]
class CustomerUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = '__all__'
        

class CustomeRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.get('password')
        confirm_password = validated_data.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=password,
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
            department=validated_data['department'],
            position=validated_data['position'],
            organization=validated_data['organization']
        )
        return user

    class Meta:
        model = CustomUser
        fields = (
           'id', 'username', 'password', 'email', 'is_staff', 'department', 'position', 'organization', 'confirm_password'
        )



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=25)
    password = serializers.CharField(
        label=('Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

class UserShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = (
            'user', 'id', 'shift', 'date', 'title', 'description'
        )

class UserShiftListSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserShift
        fields = (
            'id', 'user', 'user_name','shift', 'date', 'title', 'description'
        )

class OrganizationSerializer(serializers.ModelSerializer):
        class Meta:
            model = Organization
            fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data['user'] = user
                return data
            else:
                raise serializers.ValidationError("Incorrect email or password")
        else:
            raise serializers.ValidationError("Both email and password are required")