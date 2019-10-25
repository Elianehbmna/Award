from .models import Profile

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic','contacts'] 
        exclude=['user']    