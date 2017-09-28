from django.db import models
# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length = 250, null=True)
    avatar = models.ImageField(blank=True)
    address = models.CharField(max_length = 250, null=True)
    lat = models.IntegerField(default=0)
    lng = models.IntegerField(default=0)

    def __str__(self):
        return self.name