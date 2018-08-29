from django.test import TestCase

from attendance.models import EventAttendance
from .models import Event


# Create your tests here.
class CreateEventTests(TestCase):
    #fixtures = ['events']
    def setUp(self):
        # Create 
        pass

    def test_create_event_generate_attendance(self):
        pass
        #event = Event.object.get(id=1)
        #print(event)
        #print('testing')
