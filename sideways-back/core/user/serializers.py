from core.user.models import User
from rest_framework import serializers


# the serialized data you want to see
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'chairid',
                  'department', 'hospital', 'password', ]
