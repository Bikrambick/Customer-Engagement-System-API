from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(blank=True)
    address = models.CharField(max_length = 250, null=True)
    lat = models.IntegerField(default=0)
    lng = models.IntegerField(default=0)

    #def __str__(self):
    

User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])
