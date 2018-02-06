from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView

from .forms import MemberProfileForm 
from .models import MemberProfile, Ministry

class MemberProfileCreateView(CreateView):
    model = MemberProfile
    form_class = MemberProfileForm
    template_name = 'account_members/member_profile_add_form.html'
    success_url = reverse_lazy('home')

class MemberProfileListView(ListView):
    model = MemberProfile
    context_object_name = 'member'
    template_name = 'account_members/member_list.html'

class MinistryListView(ListView):
    model = Ministry
    context_object_name = 'ministry'
    template_name = 'ministry/ministry_list.html'
