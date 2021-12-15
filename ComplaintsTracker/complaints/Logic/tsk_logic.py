from ..models import Complaint, Task


# TODO task creation and assigning to complaint function
# TODO task closing function for assigned user and unclosing it for manager

# TODO filter function for tasks closed by user
# TODO filter function for tasks to be completed by user

def tasks_for_selected_complaint(complaint_id):
    """getting all tasks assigned to selected complaint"""
    tasks_for_complaint = Task.objects.filter(complaint=complaint_id)
    return tasks_for_complaint


def all_tasks_for_user(user):
    user_task_list = Task.objects.filter(assigned_user=user)
    return user_task_list


def count_of_tsk_created_by_me(user):
    tsk_count = Task.objects.filter(assigned_user=user).count()
    return tsk_count
