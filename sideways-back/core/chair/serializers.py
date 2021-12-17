from core.chair.models import Chair
from rest_framework import serializers


class ChairSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chair
        fields = ['id', 'model', 'location', 'status', 'destination']


# fields that are required to update chair data
class ChairUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=True, required=True)

    location = serializers.CharField(
        max_length=128
    )
    status = serializers.CharField(max_length=128)

    destination = serializers.CharField(allow_blank=True,
                                        max_length=128)

    class Meta:
        model = Chair
        fields = ['id', 'location', 'status', 'destination']
