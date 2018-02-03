from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from .forms import MemberProfileForm 
from .models import MemberProfile

# Create your views here.
class MemberProfileCreateView(CreateView):
    model = MemberProfile
    form_class = MemberProfileForm
    template_name = 'account_members/member_profile_add_form.html'
