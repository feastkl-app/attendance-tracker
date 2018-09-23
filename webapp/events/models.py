from django.db import models
from django.utils import timezone

from account_members.models import MemberProfile
from ministry_group.models import MinistryMemberGroup
from utility.models import AbstractBaseDate, AbstractBaseType


class EventType(AbstractBaseType):
    """
        Ex: Normal
    """
    pass


class Event(AbstractBaseDate):
    """
        This is the main Event model
    """
    name = models.CharField(max_length=64, blank=False)
    series = models.CharField(max_length=32, null=True)
    status = models.CharField(max_length=32, null=True)
    speaker = models.ForeignKey(
        MemberProfile, related_name='speaker', null=True)
    worship_leader = models.ForeignKey(
        MemberProfile, related_name='worship_leader', null=True)
    description = models.TextField(max_length=500, blank=True)
    event_type = models.ForeignKey(EventType, related_name='event_type')
    attending_ministries = models.ManyToManyField(MinistryMemberGroup)
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

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))
