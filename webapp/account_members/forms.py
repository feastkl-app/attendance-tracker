from django import forms

from .models import MemberProfile 

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile 
        fields = [
            'firstname',
            'lastname',
            'middlename',
            'remarks',
            'gender',
            'birthdate',
            'nationality',
            'marital_status',
            'member_since',
            'active_member' ,
            'location',
        ]
