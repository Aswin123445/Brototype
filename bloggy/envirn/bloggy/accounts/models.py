from django.db import models
from django.contrib.auth.models import AbstractUser

#creating a user model for audhentication
class CustomUserAuth(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email=models.EmailField(unique=True)
    username=models.EmailField(unique=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username' , 'phone_number' , 'password']
    def __str__(self):
        return self.email

