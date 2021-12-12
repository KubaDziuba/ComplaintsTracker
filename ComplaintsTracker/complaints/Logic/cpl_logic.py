from ..models import Complaint, Task


def latest_5_complaints():
    newest_complaints = Complaint.objects.order_by('-cpl_creation_date')[:5]
    return newest_complaints
