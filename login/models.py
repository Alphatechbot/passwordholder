from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=50, null=True, unique=True)
    phone_num = models.BigIntegerField(null=True)


