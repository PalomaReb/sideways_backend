from core.user.serializers import UserSerializer
from core.user.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):  # get to see user data
    http_method_names = ['get']
    # the data that needs to be serialized to see the user data
    serializer_class = UserSerializer
    permissions_classes = (IsAuthenticated,)  # only user authenticated
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated']
    order = ['-updated']

    def get_queryset(self):  # get user by query
        if self.request.user.is_superuser:
            return User.objects.all()

    # def get_object(self):
    #     lookup_field_value = self.kwargs[self.look_field]

        obj = User.objects.all()
        self.check_object_permissions(self.request, obj)

        return obj
