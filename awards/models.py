from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.forms.models import modelform_factory

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=1000, blank=True)
    role = models.CharField(max_length=150)
    github = models.CharField(max_length=200, blank=True)
    profile_pic=models.ImageField(upload_to='images/')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    screenshot = models.ImageField('images')
    posted_at = models.DateField(auto_now_add=True)
    repository_link = models.CharField(max_length=200, blank=True)
    live_link = models.CharField(max_length=200, blank=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')

    @property
    def get_average_visuals_rating(self):
        reviews = Review.objects.all().filter(project=self)
        visuals_ratings = []
        for review in reviews:
            visuals_ratings.append(review.visuals_rating)
        if len(visuals_ratings) != 0:
            average_visuals_rating = sum(visuals_ratings)/len(visuals_ratings)
        else:
            average_visuals_rating = 0.0

        return round(average_visuals_rating, 1)

    @property
    def get_average_functionality_rating(self):
        reviews = Review.objects.all().filter(project=self)
        functionality_ratings = []
        for review in reviews:
            functionality_ratings.append(review.functionality_rating)
        if len(functionality_ratings) != 0:
            average_functionality_rating = sum(functionality_ratings)/len(functionality_ratings)
        else:
            average_functionality_rating = 0.0

        return round(average_functionality_rating, 1)

    @property
    def get_average_content_rating(self):
        reviews = Review.objects.all().filter(project=self)
        content_ratings = []
        for review in reviews:
            content_ratings.append(review.content_rating)
        if len(content_ratings) != 0:
            average_content_rating = sum(content_ratings)/len(content_ratings)
        else:
            average_content_rating = 0.0

        return round(average_content_rating, 1)

    @property
    def get_average_usability_rating(self):
        reviews = Review.objects.all().filter(project=self)
        usability_ratings = []
        for review in reviews:
            usability_ratings.append(review.usability_rating)
        if len(usability_ratings) != 0:
            average_usability_rating = sum(usability_ratings)/len(usability_ratings)
        else:
            average_usability_rating = 0.0
        return round(average_usability_rating, 1)

    @property
    def get_overall_average_rating(self):
        return round((self.get_average_visuals_rating + self.get_average_functionality_rating + self.get_average_content_rating + self.get_average_usability_rating)/4,1)

    class Meta:
        ordering = ['posted_at']

    def __str__(self):
        return self.name



class Review(models.Model):
    review = models.TextField(max_length=1000)
    visuals_rating = models.PositiveBigIntegerField(default=10)
    functionality_rating = models.PositiveBigIntegerField(default=10)
    content_rating = models.PositiveBigIntegerField(default=10)
    usability_rating = models.PositiveBigIntegerField(default=10)
    review_date = models.DateField(auto_now_add=True)

    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews', null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews', null=True)

    @property
    def average_rating(self):
        return round((self.visuals_rating + self.functionality_rating + self.content_rating + self.usability_rating)/4,1)

