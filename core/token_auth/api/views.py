from django.contrib.auth import authenticate
from knox.models import AuthToken
from rest_framework import generics
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


class LoginView(generics.GenericAPIView):
    authentication_classes = []
    permission_classes = []
    
    username = openapi.Parameter('username', openapi.IN_HEADER, description="username", type=openapi.TYPE_STRING)
    password = openapi.Parameter('password', openapi.IN_HEADER, description="password", type=openapi.TYPE_STRING)
    @swagger_auto_schema(manual_parameters=[username, password],)
    def post(self, request, *args, **kwargs):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({
                "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({"error": "Invalid credentials"})
        
