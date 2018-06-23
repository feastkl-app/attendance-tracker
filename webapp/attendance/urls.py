from django.conf.urls import url

from .views import (
    AttendanceListView,
)

urlpatterns = [
    url(r'^$',  AttendanceListView.as_view(), name='list'),
]

