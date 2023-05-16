from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ava = models.ImageField(max_length=1224, default='user/img/avatar.png')
    bio = models.CharField(max_length=500, blank=True, default="")

    def __str__(self):
        return self.user.username
