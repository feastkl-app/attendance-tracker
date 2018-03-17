from django.conf.urls import url


from .views import (
    MemberProfileCreateView,
    MemberProfileListView,
    MemberTypeCreateView,
    MinistryTypeCreateView,
    MinistryListView,
    SampleView,
)

urlpatterns = [
    # Member
    url(r'^sample/$',SampleView.as_view(), name='sample_view'),
    url(r'^$',  MemberProfileListView.as_view(), name='member_profile_list'),
    url(r'^new/$',  MemberProfileCreateView.as_view(), name='member_profile_add'),
    #url(r'^ministry/$',  MinistryListView.as_view(), name='ministry_list'),
    #url(r'^member-type/add$',  MemberTypeCreateView.as_view(), name='member_type_create'),
    #url(r'^ministry-type/add$',  MinistryTypeCreateView.as_view(), name='ministry_type_create'),
]
