from django.db import models

from ministry_group.models import MinistryMemberGroup 
from utility.models import AbstractBaseDate, AbstractBaseType

# Create your models here.
class EventType(AbstractBaseType):
    # Ex: Normal  
    pass

class Event(AbstractBaseDate):
    name = models.CharField(max_length=64, blank=False)
    series = models.CharField(max_length=32, null=True)
    status = models.CharField(max_length=32, null=True)
    description = models.TextField(max_length=500, blank=True)
    event_type = models.ForeignKey(EventType, related_name='event_type')
    attending_ministries =  models.ManyToManyField(MinistryMemberGroup)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name

