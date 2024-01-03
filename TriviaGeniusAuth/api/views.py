from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .Serializers import RegistrationSerializer,LoginSerializer
from django.contrib.auth.models import User
from .authentication import JWTAuthentication
# Create your views here.


class RegistrationView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data={}

        if serializer.is_valid(raise_exception=True):
            account=serializer.save()
            data['username'] = account.username
            data['email']=account.email

        else:
            data = serializer.errors

        return Response(data)
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is None:
          return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({
            'username':user.username,
            'user_id':user.id,
            'token': jwt_token
            })
        
       

