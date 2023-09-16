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
    
    # username = openapi.Parameter('username', openapi.IN_BODY, description="test manual param", type=openapi.TYPE_STRING)
    # password = openapi.Parameter('password', openapi.IN_BODY, description="test manual param", type=openapi.TYPE_STRING)
    # @swagger_auto_schema(manual_parameters=[username, password],)
    @swagger_auto_schema(
            request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username','password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING)
            },),
                         operation_description='Uninstall a version of Site')
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({
                "token": AuthToken.objects.create(user)[1]
            })
        else:
            return Response({"error": "Invalid credentials"})