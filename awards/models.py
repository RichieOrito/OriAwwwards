from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    profile_pic=models.ImageField(upload_to='images/')

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    screenshot = models.ImageField('images')
    posted_at = models.DateField(auto_now_add=True)
    repository_link = models.CharField(max_length=200, blank=True)
    live_link = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')

class Review(models.Model):
    review = models.TextField(max_length=1000)
    visuals_rating = models.PositiveBigIntegerField(default=10)
    functionality_rating = models.PositiveBigIntegerField(default=10)
    content_rating = models.PositiveBigIntegerField(default=10)
    usability_rating = models.PositiveBigIntegerField(default=10)
    review_date = models.DateField(auto_now_add=True)
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews', null=True)
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews', null=True)

