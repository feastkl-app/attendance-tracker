from django.conf.urls import url


from .views import (
    MemberProfileCreateView
)
urlpatterns = [
    # Member
    url(r'^add/$',  MemberProfileCreateView.as_view(), name='member-profile-add'),
]
