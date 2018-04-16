from django.conf.urls import url

from .views import (
    EventsListView,
)

urlpatterns = [
    url(r'^$',  EventsListView.as_view(), name='list'),
]

