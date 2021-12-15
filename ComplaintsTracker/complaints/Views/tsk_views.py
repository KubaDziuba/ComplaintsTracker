from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..Logic.tsk_logic import *


def my_tasks(request):
    """showing all tasks assigned for logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    tasks_for_user = all_tasks_for_user(current_user)
    context = {'tasks_for_user': tasks_for_user,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/my_tasks.html', context)


def my_open_tasks(request):
    """showing open tasks for logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    open_tasks = users_open_tasks(current_user)
    open_tasks_count = users_open_tasks_count(current_user)
    context = {'open_tasks': open_tasks,
               'open_tasks_count': open_tasks_count,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/my_open_tasks.html', context)


def my_closed_tasks(request):
    """showing closed tasks for logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    closed_tasks = users_closed_tasks(current_user)
    closed_tasks_count = users_closed_tasks_count(current_user)
    context = {'closed_tasks': closed_tasks,
               'closed_tasks_count': closed_tasks_count,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/my_closed_tasks.html', context)


# TODO task detail view
# TODO create task view
# TODO close task view
