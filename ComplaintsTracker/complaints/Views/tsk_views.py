from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..Logic.tsk_logic import *


def my_tasks(request):
    """getting all tasks assigned for logged in user"""
    current_user = request.user.id
    tasks_for_user = all_tasks_for_user(current_user)
    context = {'tasks_for_user': tasks_for_user}
    return render(request, 'complaints/my_tasks.html', context)

# TODO task detail view
# TODO create task view
# TODO close task view
