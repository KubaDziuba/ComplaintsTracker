from ..models import Complaint, Task


def tasks_for_selected_complaint(complaint_id):
    tasks_for_complaint = Task.objects.filter(complaint=complaint_id)
    return tasks_for_complaint
