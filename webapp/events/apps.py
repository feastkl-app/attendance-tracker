from django.apps import AppConfig
from django.db.models.signals import post_save

#from events.models import Event
#from events.signals import generate_attendance


class EventsConfig(AppConfig):
    name = 'events'

    def ready(self):
        import events.signals  # noqa


