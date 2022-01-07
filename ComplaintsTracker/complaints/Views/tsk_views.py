from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from ..forms import TaskForm
from django.views import View
from django.contrib.auth.models import User
from ..Logic.tsk_logic import *


class NewTask(View):
    """Task creation form"""
    def get(self, request, complaint_id):
        form = TaskForm()
        current_complaint = complaint_id
        assigned_user = User.objects.all()
        context = {'form': form, 'assigned_user': assigned_user, 'current_complaint': current_complaint}
        return render(request, 'complaints/new_task.html', context)

    def post(self, request, complaint_id):
        form = TaskForm(request.POST)
        current_complaint = Complaint.objects.get(pk=complaint_id)
        if form.is_valid():
            new_task = Task()
            new_task.complaint = current_complaint
            new_task.tsk_name = form.cleaned_data.get('tsk_name')
            new_task.tsk_details = form.cleaned_data.get('tsk_details')
            new_task.tsk_deadline = form.cleaned_data.get('tsk_deadline')
            new_task.assigned_user = form.cleaned_data.get('assigned_user')
            new_task.is_tsk_immediate = form.cleaned_data.get('is_tsk_immediate')
            new_task.save()
            return HttpResponseRedirect(reverse('complaints:complaint_detail', args=(current_complaint.pk,)))
        context = {'form': form}
        return render(request, 'complaints/new_task.html', context)


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


def task_detail(request, task_id):
    """Detail page for selected task"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    selected_tsk = get_object_or_404(Task, pk=task_id)
    parent_cpl = selected_tsk.complaint
    context = {'selected_tsk': selected_tsk,
               'parent_cpl': parent_cpl,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/task_detail.html', context)


# TODO create task view
# TODO close task view
# TODO dates validation - task date can't be longer than cpl deadline, can't be in the past, can't be at the same day as creation
