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
    #firebase_uid = serializers.HyperlinkedRelatedField(source='profile.firebase_uid', many=False, read_only=True, view_name='users_api:user_by_uid')
    firebase_uid = serializers.CharField(source='profile.firebase_uid', required=False, allow_blank=True)
    #firebase_uid = serializers.HyperlinkedIdentityField(view_name='users_api:user_by_uid', lookup_field='profile.firebase_uid')
    address = serializers.CharField(source='profile.address', allow_blank=True, required=False)
    avatar = serializers.ImageField(source='profile.avatar', required=False, allow_null=True)
    lat = serializers.IntegerField(source='profile.lat', required=False, allow_null=True)
    lng = serializers.IntegerField(source='profile.lng', required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'avatar', 'username', 'email', 'first_name', 'last_name', 'password', 'firebase_uid', 'groups',   'address', 'lat', 'lng')
        extra_kwargs = {'url': {'view_name': 'users_api:user_detail'}}

        #'firebase_uid': {'view_name': 'users_api:user_by_uid', 'lookup_field': 'profile.firebase_uid'  }
    
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
        print(profile_data)
        #localization = requests.get('http://maps.google.com/maps/api/geocode/json?address=540 bourke st, sydney, australia')
        # create profile
        profile = UserProfile.objects.create(
            user = user,
            firebase_uid = profile_data['firebase_uid'],
            avatar = profile_data['avatar'],
            address = profile_data['address'],
            lat = profile_data['lat'],
            lng = profile_data['lng'],
        )

        return user


class UserByUidSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    firebase_uid = serializers.CharField(source='profile.firebase_uid', required=False, allow_blank=True)
    address = serializers.CharField(source='profile.address', allow_blank=True, required=False)
    avatar = serializers.ImageField(source='profile.avatar', required=False, allow_null=True)
    lat = serializers.IntegerField(source='profile.lat', required=False, allow_null=True)
    lng = serializers.IntegerField(source='profile.lng', required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('id', 'avatar', 'username', 'email', 'first_name', 'last_name', 'password', 'firebase_uid', 'groups', 'address', 'lat', 'lng')
        