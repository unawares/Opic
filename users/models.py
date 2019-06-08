from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


# TODO: Change user. This user model requires username. We need only email and password

class CustomUser(AbstractUser):

    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    # add additional fields in here

    def __str__(self):
        return self.email
# Create your models here.
