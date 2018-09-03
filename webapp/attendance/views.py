from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .models import EventAttendance

class AttendanceListView(LoginRequiredMixin, ListView):
    model = EventAttendance
    context_object_name = 'attendance_list'
    template_name = 'attendance/attendance_list.html'
    queryset = EventAttendance.objects\
        .select_related('event', 'member')\
        .all().order_by('-date_modified')

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')

        # Handling search query
        if q:
            print(f'query = {q}')
            kwargs['has_search'] = True
            kwargs['search_param'] = q
        
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        
        # Handling search query
        if q:
            queryset = queryset.filter(
                Q(event__name__icontains=q)
            )

        return queryset

