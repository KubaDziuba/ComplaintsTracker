from django.shortcuts import render
from ..models import Complaint, Task
from ..Logic.cpl_logic import *
from ..Logic.tsk_logic import *


def index(request):
    """Main view before loggin"""
    complaints = latest_5_complaints()
    context = {'complaints': complaints}
    return render(request, 'complaints/index.html', context)


def dashboard(request):
    """Main view for logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    count_of_my_cpl_list = count_of_cpls_created_by_me(current_user)
    count_of_my_task_list = count_of_tsk_created_by_me(current_user)
    count_of_open_tasks = users_open_tasks_count(current_user)
    count_of_my_open_cpls = users_open_cpls_count(current_user)
    count_of_my_closed_cpls = users_closed_cpls_count(current_user)
    count_of_my_not_approved_cpls = cpls_awaiting_approval_count(current_user)
    context = {
        "is_manager": "Manager" in current_user_groups,
        'count_of_my_cpl_list': count_of_my_cpl_list,
        'count_of_my_tsk_list': count_of_my_task_list,
        'count_of_open_tasks': count_of_open_tasks,
        'count_of_my_open_cpls': count_of_my_open_cpls,
        'count_of_my_closed_cpls': count_of_my_closed_cpls,
        'count_of_my_not_approved_cpls': count_of_my_not_approved_cpls
            }
    return render(request, 'complaints/dashboard.html', context)
