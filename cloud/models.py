from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prof')
    pin  = models.CharField(max_length=10)
    token = models.CharField(null=True, blank=True, max_length=256)

class Door(models.Model):
    open = models.BooleanField(default=False)
