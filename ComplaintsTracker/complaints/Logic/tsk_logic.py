from ..models import Complaint, Task


# TODO task creation and assigning to complaint function
# TODO task closing function for assigned user and unclosing it for manager

# TODO filter function for tasks closed by user

def tasks_for_selected_complaint(complaint_id):
    """getting all tasks assigned to selected complaint"""
    tasks_for_complaint = Task.objects.filter(complaint=complaint_id)
    return tasks_for_complaint


def all_tasks_for_user(user):
    """getting all tasks assigned for logged in user"""
    user_task_list = Task.objects.filter(assigned_user=user)
    return user_task_list


def count_of_tsk_created_by_me(user):
    """getting number of tasks assigned for logged in user"""
    tsk_count = Task.objects.filter(assigned_user=user).count()
    return tsk_count


def users_open_tasks(user):
    """getting list of open tasks for user"""
    open_tasks_for_user = Task.objects.filter(assigned_user=user, is_tsk_finished=False)
    return open_tasks_for_user


def users_open_tasks_count(user):
    """getting number of open tasks for user"""
    open_tasks_for_user_count = Task.objects.filter(assigned_user=user, is_tsk_finished=False).count()
    return open_tasks_for_user_count


def users_closed_tasks(user):
    """getting list of closed tasks for user"""
    closed_tasks_for_user = Task.objects.filter(assigned_user=user, is_tsk_finished=True)
    return closed_tasks_for_user


def users_closed_tasks_count(user):
    """getting number of closed tasks for user"""
    closed_tasks_for_user_count = Task.objects.filter(assigned_user=user, is_tsk_finished=True).count()
    return closed_tasks_for_user_count
