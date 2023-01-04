from .models import CustomUser, UserShift
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'email', 'username', 'date_joined', 'last_login',
            'is_admin', 'is_staff', 'department', 'position'
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



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=25)
    password = serializers.CharField(
        label=('Password'),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )
    def validate(self, data):
        import pdb; pdb.set_trace()

class UserShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserShift
        fields = (
            'user', 'id'
            'shift', 'date', 'title', 'description'
        )

# class UserShiftListSerializer(serializers.ModelSerializer):
