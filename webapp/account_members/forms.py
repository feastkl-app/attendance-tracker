from django import forms

from .models import MemberProfile, MemberType, MinistryType  

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

class MemberTypeForm(forms.ModelForm):
    class Meta:
        model = MemberType
        fields = [ 'name', 'remarks' ]

class MinistryTypeForm(forms.ModelForm):
    class Meta:
        model = MinistryType
        fields = [ 'name', 'remarks' ]
