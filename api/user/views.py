from django.shortcuts import render
from django.http import JsonResponse
from user.models import User, Profile

from user.serializer import UserSerializer,MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.response import Response
from rest_framework.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = ([AllowAny])
    serializer_class = RegisterSerializer


# # Get All Routes

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         '/api/token/',
#         '/api/register/',
#         '/api/token/refresh/'
#     ]
#     return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    if request.method == 'GET':
        context = f"hey {request.user}, Your are seeing a GET response"
        return Response({'response': context}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.POST.get("text")
        context = f"hey {request.user}, your text is {text} "
        return Response({'response': context}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)