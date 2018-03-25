from django.conf.urls import url

from .views import (
    MinistryGroupListView,
)

urlpatterns = [
    url(r'^$',  MinistryGroupListView.as_view(), name='list'),
]
