from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=['bio','profilepic','email'] 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields=['image','projectName','description','link','screenshot1','screenshot2','screenshot3']