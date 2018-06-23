from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .models import EventAttendance

class AttendanceListView(LoginRequiredMixin, ListView):
    model = EventAttendance
    context_object_name = 'attendance'
    template_name = 'attendance/attendance_list.html'

