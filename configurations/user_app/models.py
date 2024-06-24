from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=55, unique=False)
    nickname = models.CharField(max_length=55)
    name_profile_picture = models.CharField(max_length=500, null=True)
    profile_picture = models.ImageField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return self.nickname+" : "+str(self.id )
    


class PasswordResetData(models.Model):
    encoded_pk = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

