from rest_framework import serializers 
from .models import User
from django.shortcuts import get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import Group
#import requests

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    address = serializers.CharField(source='profile.address')
    avatar = serializers.ImageField(source='profile.avatar')
    lat = serializers.IntegerField(source='profile.lat')
    lng = serializers.IntegerField(source='profile.lng')

    class Meta:
        model = User
        fields = ('id', 'url', 'avatar', 'username', 'groups', 'email', 'first_name', 'last_name', 'password', 'address', 'lat', 'lng')
        extra_kwargs = {'url': {'view_name': 'users_api:user_detail'}}
    
    def create(self, data):
        # create user 
        user = User.objects.create(
            email = data['email'],
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            password = data['password'],
        )

        profile_data = data.pop('profile')
        #localization = requests.get('http://maps.google.com/maps/api/geocode/json?address=540 bourke st, sydney, australia')
        # create profile
        profile = UserProfile.objects.create(
            user = user,
            avatar = profile_data['avatar'],
            address = profile_data['address'],
            lat = profile_data['lat'],
            lng = profile_data['lng'],
        )

        return user


