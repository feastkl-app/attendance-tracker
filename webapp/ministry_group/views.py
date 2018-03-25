from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, UpdateView

from .models import Ministry, MinistryMember

class MinistryGroupListView(LoginRequiredMixin, ListView):
    model = Ministry
    template_name = 'ministry_group/ministry_group_list.html'
    context_object_name = 'ministry_group'
#
#    def get_context_data(self, **kwargs):
#         kwargs['total_count'] = MemberProfile.objects.count()
#         return super().get_context_data(**kwargs)
