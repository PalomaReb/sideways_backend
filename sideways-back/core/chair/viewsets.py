from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from core.chair.models import Chair
from core.chair.serializers import ChairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from core.chair.serializers import ChairSerializer, ChairUpdateSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.response import Response


class ChairViewSet(viewsets.ModelViewSet):  # viewset to view all or one chair
    http_method_names = ['get']
    # data that has been serialized to work with in class
    serializer_class = ChairSerializer
    permissions_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Chair.objects.all()


class ChairUpdateViewSet(ModelViewSet):  # updating chair
    serializer_class = ChairUpdateSerializer  # serialized data
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        # update the data that is being sent
        serializer = self.get_serializer(data=request.data)

        try:  # if all data is valid, update the chair data
            serializer.is_valid(raise_exception=True)
            Chair.objects.filter(id=serializer.validated_data['id']).update(
                location=serializer.validated_data['location'])
            Chair.objects.filter(id=serializer.validated_data['id']).update(
                status=serializer.validated_data['status'])
            Chair.objects.filter(id=serializer.validated_data['id']).update(
                destination=serializer.validated_data['destination'])
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(request.data, status=status.HTTP_200_OK)
