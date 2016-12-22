from django.conf.urls import url

from .views import EntryListView, EntryDetailView

urlpatterns = [
    url(r'^entries/$', EntryListView.as_view(), name="bloglist"),
    url(r'^entries/(?P<pk>[0-9]+)?', EntryDetailView.as_view(), name="blogdetail"),
]
