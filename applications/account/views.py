# from applications.account.send_mail import sent_hello

from applications.account.send_mail import sent_hello
from applications.account.serializers import (ChangePasswordSerializer, ForgotPasswordCompleteSerializer, ForgotPasswordSerilizer, LoginSerializer, RegisterSerializer)
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

User = get_user_model()

class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались.''Вам отправлено письмо с активацией.', status=201)


class LoginApiView(ObtainAuthToken):
    serializer_class = LoginSerializer


class LogoutApiView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились!')


class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен')

@api_view(['POST'])
def send_hello_api_view(request):
    sent_hello('maksatovch.1@gmail.com')
    return Response('Письмо отправлен!')

class ActivationApiView(APIView):
    def get(self, request, activation_code):
        try:    
            user = User.objects.get(activation_code=activation_code)
            user.is_active=True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'успешно'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=status.HTTP_400_BAD_REQUEST)   


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerilizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправленно письмо для восстановление пароля')


class ForgotPasswordCompleteAPIView(APIView):
    def post(self, request):
        serializser = ForgotPasswordCompleteSerializer(data=request.data)
        serializser.is_valid(raise_exception=True)
        serializser.set_new_password()
        return Response('пароль успешно обновлен')        