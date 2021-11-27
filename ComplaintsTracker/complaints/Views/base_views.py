from django.shortcuts import render
from ..models import Complaint, Task


# Create your views here.
def index(request):
    complaints = Complaint.objects.all()
    context = {'complaints': complaints}
    return render(request, 'complaints/index.html', context)


def dashboard(request):
    return render(request, 'complaints/dashboard.html')
