from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView

from .forms import MemberProfileForm, MemberTypeForm
from .models import MemberProfile, MemberType

class SampleView(TemplateView):
    template_name = 'index.html'

class MemberProfileCreateView(LoginRequiredMixin, CreateView):
    model = MemberProfile
    form_class = MemberProfileForm
    template_name = 'account_members/member_create.html'
    success_url = reverse_lazy('members:member_profile_list')

class MemberProfileListView(LoginRequiredMixin, ListView):
    model = MemberProfile
    context_object_name = 'members'
    template_name = 'account_members/member_list.html'

    def get_context_data(self, **kwargs):
         kwargs['total_count'] = MemberProfile.objects.count()
         return super().get_context_data(**kwargs)

class MemberProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = MemberProfile
    context_object_name = 'member'
    template_name = 'account_members/member_update.html'
    fields = (
        'firstname', 
        'middlename', 
        'lastname', 
        'primary_role',
        'email', 
        'contact_number1', 
        'contact_number2',
        'gender',
        'nationality',
        'birthdate',
        'remarks',
        'marital_status',
        'member_since',
        'location',
    )
    success_url = reverse_lazy('members:member_profile_list')

class MemberProfileDetailView(LoginRequiredMixin, DetailView):
    model = MemberProfile
    context_object_name = 'member'
    template_name = 'account_members/member_details.html'
