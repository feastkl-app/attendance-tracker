from django.conf.urls import url

from .views import (
    EventsCreateView,
    EventsDetailView,
    EventsListView,
)

urlpatterns = [
    url(r'^$',  EventsListView.as_view(), name='list'),
    url(r'^new/$',  EventsCreateView.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$',  EventsDetailView.as_view(), name='detail'),
]

