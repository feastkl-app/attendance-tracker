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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ministry_head = MinistryMember.objects.filter(
            ministrymembergroup__pk=self.kwargs['pk'], member_type__name='Ministry Head'
        )
        if ministry_head:
            context['ministry_head'] = str(ministry_head[0].member)

        return context
