from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class LoginView(APIView):

    def post(self, request):
        email = request.data.get('email', None)
        # EJ: {"email": "gianca@gmail.com", "password": "asdasd"}
        password = request.data.get('password', None)

        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return Response(
                {'Username:': UserSerializer(user).data['username'],
                 'email:': UserSerializer(user).data['email'],
                 'first_name:': UserSerializer(user).data['first_name'],
                 'last_name:': UserSerializer(user).data['last_name']},
                status=status.HTTP_200_OK)

        return Response(
            status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return Response(status=status.HTTP_200_OK)


class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
