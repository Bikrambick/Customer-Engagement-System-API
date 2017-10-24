from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserProfile, User
from .serializers import UserSerializer, UserByUidSerializer

from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes

#@authentication_classes((TokenAuthentication, SessionAuthentication))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
class UserByUid(APIView):
    def get(self, request, uid):
        user = get_object_or_404(UserProfile, firebase_uid = uid)
        serializer = UserByUidSerializer(user.user)
        return Response(serializer.data)



