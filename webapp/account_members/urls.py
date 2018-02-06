from django.conf.urls import url


from .views import (
    MemberProfileCreateView,
    MemberProfileListView,
    MinistryListView,
)

urlpatterns = [
    # Member
    url(r'^$',  MemberProfileListView.as_view(), name='member-profile-list'),
    url(r'^add/$',  MemberProfileCreateView.as_view(), name='member-profile-add'),
    url(r'^ministry/$',  MinistryListView.as_view(), name='ministry-list'),
]
