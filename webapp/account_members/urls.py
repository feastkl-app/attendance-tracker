from django.conf.urls import url


from .views import (
    MemberProfileCreateView,
    MemberProfileListView,
)

urlpatterns = [
    # Member
    url(r'^$',  MemberProfileListView.as_view(), name='member-profile-list'),
    url(r'^add/$',  MemberProfileCreateView.as_view(), name='member-profile-add'),
]
