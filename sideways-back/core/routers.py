# RUTAS PARA LAS DIRECIONES DEL BACKEND

from rest_framework.routers import SimpleRouter
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from core.chair.viewsets import ChairViewSet, ChairUpdateViewSet


routes = SimpleRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet,
                basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


# USER
routes.register(r'user', UserViewSet, basename='user')

# CHAIR
routes.register(r'chair/view', ChairViewSet, basename='chair')
routes.register(r'chair/update', ChairUpdateViewSet, basename='chair-update')

urlpatterns = [
    *routes.urls
]
