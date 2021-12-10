from django.shortcuts import render
from ..models import Complaint, Task
from ..Logic.generic import *
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    complaints = Complaint.objects.all()
    context = {'complaints': complaints}
    return render(request, 'complaints/index.html', context)


def dashboard(request):
    current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
            "is_manager": "Manager" in current_user_groups,
    }
    return render(request, 'complaints/dashboard.html', context)
