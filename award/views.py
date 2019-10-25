# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
# from .forms import ImageForm,UpdateProfile,CommentForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

