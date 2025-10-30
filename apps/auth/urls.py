from django.urls import path
from .controller import AuthController

_authController = AuthController()

urlpatterns = [
    path("login", _authController.login, name="login"),
    path("register", _authController.register, name="register"),
]