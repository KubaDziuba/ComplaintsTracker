from ..models import Complaint, Task


def latest_5_complaints():
    """getting last 5 complaints for index view before login"""
    newest_complaints = Complaint.objects.order_by('-cpl_creation_date')[:5]
    return newest_complaints


def cpls_created_by_me(user):
    """getting cpls created bu logged user"""
    my_cpls = Complaint.objects.filter(reporting_user=user)
    return my_cpls


def count_of_cpls_created_by_me(user):
    """getting number of cpls created by logged user"""
    cpl_count = Complaint.objects.filter(reporting_user=user).count()
    return cpl_count


def users_open_cpls(user):
    """getting list of open complaints for user"""
    open_cpls_for_user = Complaint.objects.filter(reporting_user=user, is_cpl_finished=False)
    return open_cpls_for_user


def users_open_cpls_count(user):
    """getting number of open complaints for user"""
    open_cpls_for_user_count = Complaint.objects.filter(reporting_user=user, is_cpl_finished=False).count()
    return open_cpls_for_user_count


def users_closed_cpls(user):
    """getting list of closed complaints for user"""
    closed_cpls_for_user = Complaint.objects.filter(reporting_user=user, is_cpl_finished=True)
    return closed_cpls_for_user


def users_closed_cpls_count(user):
    """getting number of closed complaints for user"""
    closed_cpls_for_user_count = Complaint.objects.filter(reporting_user=user, is_cpl_finished=True).count()
    return closed_cpls_for_user_count


# Functions for Managers
def cpls_awaiting_approval(user):
    """getting complaints awaiting for manager's approval"""
    opened_cpls_awaiting_users_approval = Complaint.objects.filter(closing_user=user, is_cpl_finished=False)
    return opened_cpls_awaiting_users_approval


def cpls_awaiting_approval_count(user):
    """getting count of complaints awaiting for manager's approval"""
    opened_cpls_awaiting_users_approval_count = Complaint.objects.filter(closing_user=user, is_cpl_finished=False).count()
    return opened_cpls_awaiting_users_approval_count


def approved_cpls(user):
    """getting complaints approved by manager"""
    managers_approved_cpls = Complaint.objects.filter(closing_user=user, is_cpl_finished=True)
    return managers_approved_cpls


def approved_cpls_count(user):
    """getting complaints approved by manager count"""
    managers_approved_cpls_count = Complaint.objects.filter(closing_user=user, is_cpl_finished=True).count()
    return managers_approved_cpls_count



# TODO function to create complaint
# TODO function to approve complaint by manager

