from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .models import Ministry, MinistryMember, MinistryMemberGroup

class MinistryGroupListView(LoginRequiredMixin, ListView):
    model = MinistryMemberGroup
    template_name = 'ministry_group/ministry_group_list.html'
    context_object_name = 'ministry_group'


class MinistryGroupDetailView(LoginRequiredMixin, DetailView):
    model = MinistryMemberGroup
    context_object_name = 'ministry_member_group'
    template_name = 'ministry_group/ministry_group_details.html'
