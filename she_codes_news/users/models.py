from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
#    this is where I would put custom fields
    pass
    def __str__(self):
        return self.username