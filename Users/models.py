from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    gcm_token = models.CharField(max_length=150)


class Location(models.Model):
    username = models.CharField(max_length=55)
    long = models.DecimalField(max_digits=25, decimal_places=25)
    lat = models.DecimalField(max_digits=25, decimal_places=25)


class GPSRequest(models.Model):
    username_requester = models.CharField(max_length=55)
    username_requested = models.CharField(max_length=55)
