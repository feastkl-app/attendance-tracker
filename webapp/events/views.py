from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .forms import EventForm
from .models import Event

class EventsCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/events_create.html'
    success_url = reverse_lazy('events:list')

class EventsListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    queryset = Event.objects\
        .prefetch_related('attending_ministries__ministry')\
        .select_related('speaker', 'worship_leader')\
        .all().order_by('-date_modified')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['upcoming_events'] = Event.objects.filter(start_date__gte=timezone.now()) 

        return context

class EventsDetailView(LoginRequiredMixin, DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'events/events_details.html'
