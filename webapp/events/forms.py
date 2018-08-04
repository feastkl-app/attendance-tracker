from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event 
        fields = [
            'name',
            'series',
            'status',
            'speaker',
            'worship_leader',
            'description',
            'event_type',
            'attending_ministries',
            'start_date',
            'end_date',
            'location',
        ]
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date'}),
            'end_date': forms.TextInput(attrs={'type': 'date'}),
        }
