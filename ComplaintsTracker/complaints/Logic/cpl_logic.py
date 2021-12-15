from ..models import Complaint, Task


def latest_5_complaints():
    newest_complaints = Complaint.objects.order_by('-cpl_creation_date')[:5]
    return newest_complaints


def cpls_created_by_me(user):
    my_cpls = Complaint.objects.filter(reporting_user=user)
    return my_cpls


def count_of_cpls_created_by_me(user):
    cpl_count = Complaint.objects.filter(reporting_user=user).count()
    return cpl_count

# TODO function to create complaint
# TODO function to approve complaint by manager

# TODO filter function for complaints created by user which aren't yet approved
# TODO filter function for complaints already approved by given manager
# TODO filter function for complaints yet to be closed by given manager
