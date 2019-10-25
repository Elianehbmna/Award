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
    bio=models.IntegerField(max_length=100,blank=True,default="your contacts")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    # @classmethod
    # def search_by_name(cls,search_term):
    #     news = cls.objects.filter(user__username__icontains = search_term)
    #     return news

