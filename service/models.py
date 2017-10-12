from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 250, blank=True)
    avatar = models.ImageField(blank=True)
    address = models.CharField(max_length = 250, blank=True)
    lat = models.IntegerField(null=True)
    lng = models.IntegerField(null=True)

    def __str__(self):
        return self.name