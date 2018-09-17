from django import forms

from .models import MemberProfile, MemberType

class MemberProfileForm(forms.ModelForm):
    class Meta:
        model = MemberProfile
        fields = [
            'firstname',
            'lastname',
            'middlename',
            'primary_role',
            'remarks',
            'gender',
            'birthdate',
            'nationality',
            'marital_status',
            'member_since',
            'active_member' ,
            'location',
        ]
        widgets = {
            'birthdate': forms.TextInput(attrs={'type': 'date'}),
            'member_since': forms.TextInput(attrs={'type': 'date'}),
        }

class MemberTypeForm(forms.ModelForm):
    class Meta:
        model = MemberType
        fields = [ 'name', 'remarks' ]

