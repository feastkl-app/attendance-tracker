from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, TemplateView

from .forms import MemberProfileForm, MemberTypeForm, MinistryTypeForm
from .models import MemberProfile, Ministry, MemberType, MinistryType

class SampleView(TemplateView):
    template_name = 'index.html'

class MemberProfileCreateView(CreateView):
    model = MemberProfile
    form_class = MemberProfileForm
    template_name = 'account_members/member_profile_add_form.html'
    success_url = reverse_lazy('home')

class MemberProfileListView(ListView):
    model = MemberProfile
    context_object_name = 'members'
    template_name = 'account_members/member_list.html'

    def get_context_data(self, **kwargs):
         kwargs['total_count'] = MemberProfile.objects.count()
         return super().get_context_data(**kwargs)


class MinistryListView(ListView):
    model = Ministry
    context_object_name = 'ministry'
    template_name = 'ministry/ministry_list.html'

class MemberTypeCreateView(CreateView):
    model = MemberType
    form_class = MemberTypeForm
    template_name = 'member_type/member_type_add_form.html'
    success_url = reverse_lazy('home')

class MinistryTypeCreateView(CreateView):
    model = MinistryType
    form_class = MinistryTypeForm
    template_name = 'ministry_type/ministry_type_add_form.html'
    success_url = reverse_lazy('home')
