from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
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
    queryset = MemberProfile.objects.select_related('primary_role').all()

    def get_context_data(self, **kwargs):
        kwargs['total_count'] = MemberProfile.objects.count()
        q = self.request.GET.get('q')

        # Handling search query
        if q:
            kwargs['has_search'] = True
            kwargs['search_param'] = q
        
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        
        # Handling search query
        if q:
            queryset = queryset.filter(
                Q(firstname__icontains=q) |
                Q(lastname__icontains=q)
            )

        return queryset

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
