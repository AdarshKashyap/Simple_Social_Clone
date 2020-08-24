from django.db import models
from django.contrib import auth

# Create your models here.
# Updating the User model from django.contrib.auth package as per our need
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
