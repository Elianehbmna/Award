from .models import Profile,Project,Rating
from django import forms

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic','email'] 
        exclude=['user']   
class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['image','projectName','description','link','screenshot1','screenshot2','screenshot3'] 
        exclude=['profile','postdate','design','usability','content','overall_score','avatar','country']

class RatingForm(forms.ModelForm):
     class Meta:
         model=Rating
         fields=['design','content','usability']
         exclude=['overall_score','project','profiles','users']

