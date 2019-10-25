from .models import Profile
from django import forms

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic','email'] 
        exclude=['user']    