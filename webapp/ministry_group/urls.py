from django.conf.urls import url

from .views import (
    MinistryGroupDetailView,
    MinistryGroupListView,
)

urlpatterns = [
    url(r'^$',  MinistryGroupListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',  MinistryGroupDetailView.as_view(), name='details'),
]
