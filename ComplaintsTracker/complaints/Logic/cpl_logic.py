from ..models import Complaint, Task
from django.contrib.auth.models import User


def latest_5_complaints():
    newest_complaints = Complaint.objects.order_by('-cpl_creation_date')[:5]
    return newest_complaints


def cpls_created_by_me(user):
    my_cpls = Complaint.objects.filter(reporting_user=user)
    return my_cpls


def count_of_cpls_created_by_me(user):
    cpl_count = Complaint.objects.filter(reporting_user=user).count()
    return cpl_count
