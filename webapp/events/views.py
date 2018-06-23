from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .models import Event

class EventsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/events_list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['upcoming_events'] = Event.objects.filter(start_date__gte=timezone.now()) 
        print(context)

        return context
