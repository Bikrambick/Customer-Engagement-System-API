from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    firebase_uid = models.CharField(max_length = 250, blank=True) 
    avatar = models.ImageField(blank=True)
    address = models.CharField(max_length = 250, blank=True)
    lat = models.IntegerField( null=True)
    lng = models.IntegerField( null=True)

    #def __str__(self):
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])
