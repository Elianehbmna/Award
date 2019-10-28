# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime as dt
from tinymce.models import HTMLField

class Profile(models.Model):
    bio=models.TextField(max_length=100,blank=True,default="bio please...")
    profilepic=models.ImageField(upload_to='profile/', blank = True,default='../static/images/bad-profile-pic-2.jpeg')
    email=models.CharField(blank=True,max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user


class Project(models.Model):
    image = models.ImageField(upload_to='landingpage/', blank=True)
    projectName = models.CharField(max_length =30)
    description= models.TextField(max_length =300)
    link=models.CharField(max_length=40)
    screenshot1=models.ImageField(upload_to='screenshots/', blank=True)
    screenshot2=models.ImageField(upload_to='screenshots/', blank=True)
    screenshot3=models.ImageField(upload_to='screenshots/', blank=True)
    design=models.IntegerField(blank=True,default=0)
    usability=models.IntegerField(blank=True,default=0)
    content=models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to='avatars/')
    profile= models.ForeignKey(User,on_delete=models.CASCADE)
    user_profile=models.ForeignKey(Profile)
    likes=models.ManyToManyField(User,related_name = 'likes',blank=True)

    def __str__(self):
        return self.projectName
 
    
    @classmethod
    def search_by_projectname(cls,search_term):
        name = cls.objects.filter(projectName__icontains = search_term)
        return name

    @classmethod
    def save_image(self):
        self.save()
    @classmethod
    def delete_image(self):
        self.delete()
    

class Rating(models.Model):
    design = models.IntegerField(blank=True,default=0)
    usability = models.IntegerField(blank=True,default=0)
    content = models.IntegerField(blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    profiles = models.ForeignKey(Profile,on_delete=models.CASCADE)
    