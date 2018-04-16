from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        print(self.request.user)
        print(dir(self.request.user))
        #print(self.request.user.member_profile)
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context


# Create your views here.
