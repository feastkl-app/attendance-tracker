from django.conf.urls import url

from .views import (
    EventsCreateView,
    EventsListView,
)

urlpatterns = [
    url(r'^$',  EventsListView.as_view(), name='list'),
    url(r'^new/$',  EventsCreateView.as_view(), name='new'),
]

