from .models import User , UserType, UserAddress
from rest_framework import serializers
from django.contrib.auth.models import Permission
from rest_framework_simplejwt.tokens import RefreshToken

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'user_type')


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['name']
    

class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'


class UserSerializerWithToken(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    authority = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email','authority', 'token']

    def get_authority(self, obj):
        if obj.is_staff:
            return "admin"
        return obj.user_type.values_list("name", flat=True)

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)