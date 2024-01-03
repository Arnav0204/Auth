from django.contrib import admin
from django.urls import path
from .views import RegistrationView,LoginView

urlpatterns = [
    path('Login/', LoginView.as_view(),name="login"),
    path('Register/',RegistrationView.as_view(),name="register"),
]
