from django.shortcuts import render
from ..models import Complaint, Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ComplaintListView(ListView):
    model = Complaint


class ComplaintDetailView(DetailView):
    model = Complaint
