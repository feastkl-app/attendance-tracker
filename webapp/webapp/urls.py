from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from dashboard import views as dashboard_view

urlpatterns = [
    url(r'^$', dashboard_view.HomePageView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    # Attendance
    url(r'^attendance/', include('attendance.urls', namespace='attendance')),

    # Account members
    url(r'^members/', include('account_members.urls', namespace='members')),

    # Events
    url(r'^events/', include('events.urls', namespace='events')),

    # Ministry group
    url(r'^ministry-group/', include('ministry_group.urls', namespace='ministry_group')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
