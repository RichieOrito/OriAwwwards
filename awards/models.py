from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    profile_pic=models.ImageField(upload_to='images/')


