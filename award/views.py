# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile,User,Project,Rating
from .forms import UpdateProfile,ProjectForm,RatingForm
# from decouple import config,Csv
import datetime as dt
from django.http import JsonResponse
import json
from django.db.models import Max
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    date = dt.date.today()
    winners=Project.objects.all()
    caraousel = Project.objects.order_by('-overall_score')
    nominees=Project.objects.all()
    
    resources=Project.objects.all()
    

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
        print(current_user)
    except ObjectDoesNotExist:
        return redirect('profile')

    return render(request,'index.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date,"nominees":nominees,"resources":resources})

  

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):
    '''
    Method that fetches a users profile page
    '''
    user=User.objects.get(pk=profile_id)
    project = Project.objects.filter(profile = profile_id)
    title = User.objects.get(pk = profile_id).username
    profile = Profile.objects.filter(user = profile_id)
    return render(request,"all-views/profile.html",{"profile":profile,"title":title,"project":project})

@login_required(login_url='/accounts/login/')
def updateProfile(request):

    current_user=request.user
    if request.method =='POST':
        if Profile.objects.filter(user_id=current_user).exists():
            form = UpdateProfile(request.POST,request.FILES,instance=Profile.objects.get(user_id = current_user))
        else:
            form=UpdateProfile(request.POST,request.FILES)
        if form.is_valid():
          profile=form.save(commit=False)
          profile.user=current_user
          profile.save()
          return redirect('profile',current_user.id)
    else:

        if Profile.objects.filter(user_id = current_user).exists():
           form=UpdateProfile(instance =Profile.objects.get(user_id=current_user))
        else:
            form=UpdateProfile()

    return render(request,'all-views/update.html',{"form":form})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(user = request.user.id)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.user_profile = profile
            project.save()
        return redirect('profile',current_user.id)

    else:
        form = ProjectForm()

    return render(request,'create-project/new-project.html',{"form":form})


def directory(request):
    date =dt.date.today()
    current_user =request.user
    profile=Profile.objects.get(user=current_user)
    winners=Project.objects.all()
    caraousel=Project.objects.get(id=2)
    return render(request,'directory.html',{"winners":winners,"profile":profile,"caraousel":caraousel,"date":date})

@login_required(login_url='/accounts/login/')
def site(request,site_id):
    current_user = request.user
    profile =Profile.objects.get(user=current_user)

    try:
        project = Project.objects.get(id=site_id)
    except:
        raise ObjectDoesNotExist()

    
    ratings = Rating.objects.filter(project_id=site_id)
    design = Rating.objects.filter(project_id=site_id).values_list('design',flat=True)
    usability = Rating.objects.filter(project_id=site_id).values_list('usability',flat=True)
    content = Rating.objects.filter(project_id=site_id).values_list('content',flat=True)
    total_design=0
    total_usability=0
    total_content = 0
    print(design)
    for rate in design:
        total_design+=rate
    

    for rate in usability:
        total_usability+=rate
    print(total_usability)

    for rate in content:
        total_content+=rate
    

    overall_score=(total_design+total_content+total_usability)/4

    

    project.design = total_design
    project.usability = total_usability
    project.content = total_content
    project.overall_score = overall_score

    project.save()

    

    if request.method =='POST':
        form = RatingForm(request.POST,request.FILES)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.project= project
            rating.profiles = profile
            rating.overall_score = (rating.design+rating.usability+rating.content)/2
            rating.save()
    else:
        form = RatingForm()

    return render(request,"site.html",{"project":project,"profile":profile,"ratings":ratings,"form":form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'proname' in request.GET and request.GET["proname"]:
        search_term = request.GET.get("proname")
        searched_user = Project.search_by_projectname(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_user})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message}) 


class ProfileList(APIView):

    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = ProfileSerializer(all_merch, many=True)
        return Response(serializers.data)

class ProjectList(APIView):

    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = ProjectSerializer(all_merch, many=True)
        return Response(serializers.data)



