from django.db import models
from account_members.models import MemberProfile
from events.models import Event 
from utility.models import AbstractBaseDate

class EventAttendance(AbstractBaseDate):
    member = models.ForeignKey(MemberProfile, related_name='member')
    event = models.ForeignKey(Event, related_name='event')
    remarks = models.CharField(max_length=64, blank=True)
    attended = models.NullBooleanField()

    class Meta:
        verbose_name_plural = u"Event Attendance"

    def __str__(self):
        return "Event: %s (Attendance)" %(str(self.event))

