from django.contrib.auth.models import AbstractUser
from django.db import models


# TODO: Change user. This user model requires username. We need only email and password

class CustomUser(AbstractUser):
    # add additional fields in here
    def __str__(self):
        return self.email
# Create your models here.
