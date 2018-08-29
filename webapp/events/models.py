from django.db import models
from django.db.models import signals
from django.utils import timezone


from account_members.models import MemberProfile, MemberType
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
    speaker = models.ForeignKey(MemberProfile, related_name='speaker', null=True)
    worship_leader = models.ForeignKey(MemberProfile, related_name='worship_leader', null=True)
    description = models.TextField(max_length=500, blank=True)
    event_type = models.ForeignKey(EventType, related_name='event_type')
    attending_ministries =  models.ManyToManyField(MinistryMemberGroup)
    start_date = models.DateTimeField(blank=False)
    end_date = models.DateTimeField(blank=False)
    location = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.name


    @property
    def event_status(self):
        """
            returns event status - RECENT, ONGOING, UPCOMING
        """
        if timezone.now() > self.end_date:
            return 'RECENT'
        elif timezone.now() >= self.start_date:
            return 'ONGOING'
        else:
            return 'UPCOMING'


