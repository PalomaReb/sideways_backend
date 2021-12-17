from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

from core.user.serializers import UserSerializer
from core.user.models import User


# call for token serializer to make sure user has token
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)  # validate data

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


# calls for the user serializer data in order to use in this class
class RegisteredSerializer(UserSerializer):
    # register fields characteristics
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True, required=True)
    department = serializers.CharField(
        max_length=128, write_only=True, required=True
    )
    hospital = serializers.CharField(
        max_length=128, write_only=True, required=True
    )
    chairid = serializers.IntegerField(required=True)

    email = serializers.EmailField(
        required=True, write_only=True, max_length=128)

    class Meta:  # fields that must be included in the creation on the user
        model = User
        fields = ['id', 'email', 'chairid',
                  'department', 'hospital', 'password', ]

    def create(self, validated_data):
        try:
            # obtain all objects of the user and validate the data
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user
