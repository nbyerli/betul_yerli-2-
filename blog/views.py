from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.models import BlogEntry


class EntryDetailView(DetailView):
    model=BlogEntry

class EntryListView(ListView):
    model=BlogEntry
