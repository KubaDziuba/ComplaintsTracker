from django.shortcuts import render
from ..models import Complaint, Task
from ..Logic.cpl_logic import *
from django.contrib.auth.models import User


# Main view
def index(request):
    complaints = latest_5_complaints()
    context = {'complaints': complaints}
    return render(request, 'complaints/index.html', context)


# View of logged in user
def dashboard(request):
    # getting list of groups user belongs to
    current_user_groups = request.user.groups.values_list("name", flat=True)
    context = {
            "is_manager": "Manager" in current_user_groups,
    }
    return render(request, 'complaints/dashboard.html', context)
