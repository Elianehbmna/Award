from .models import Profile
from django import forms

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic','contacts'] 
        exclude=['user']    