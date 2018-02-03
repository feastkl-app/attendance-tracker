from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from event_attendance import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Account members
    url(r'^members/', include('account_members.urls', namespace='members')),
]
