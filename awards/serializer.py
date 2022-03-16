from django.db.models import fields
from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'