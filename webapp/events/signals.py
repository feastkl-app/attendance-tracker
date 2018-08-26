from django.db.models.signals import post_save
from django.dispatch import receiver

from attendance.models import EventAttendance  
from .models import Event

@receiver(post_save, sender=Event)
def generate_attendance(sender, instance, created, **kwargs):
    print('Signal: Generate attendance')
    if created:
        unique_member_list = _get_unique_members_from_event_created(instance)
        attendance_list = _generate_attendance_from_event_created_and_members(instance, unique_member_list)

        # Create attendance (bulk)
        EventAttendance.objects.bulk_create(attendance_list)

        
def _get_unique_members_from_event_created(event_instance):
    member_list = []

    # Extract members from event created by ministries and unique
    for ministries in event_instance.attending_ministries.all(): 
        for member in ministries.ministry_member.all():
            member_list.append(member.member)

    return list(set(member_list))

def _generate_attendance_from_event_created_and_members(event_instance, members):
    attendance_list = []

    for member in members:
        attendance = EventAttendance(event=event_instance, member=member)
        attendance_list.append(attendance)

    return attendance_list
