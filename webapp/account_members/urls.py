from django.conf.urls import url

from .views import (
    MemberProfileCreateView,
    MemberProfileDetailView,
    MemberProfileListView,
    MemberProfileUpdateView,
)

urlpatterns = [
    url(r'^$',  MemberProfileListView.as_view(), name='member_profile_list'),
    url(r'^new/$',  MemberProfileCreateView.as_view(), name='member_profile_add'),
    url(r'^(?P<pk>\d+)/$',  MemberProfileDetailView.as_view(), name='member_profile_details'),
    url(r'^(?P<pk>\d+)/edit/$',  MemberProfileUpdateView.as_view(), name='member_profile_update'),
]

