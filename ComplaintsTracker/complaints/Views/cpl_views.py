from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.views.generic.list import ListView
from ..Logic.cpl_logic import *
from ..forms import ComplaintForm
from django.views import View
from django.contrib.auth.models import User


class ComplaintListView(ListView):
    """List view of all complaints created by all users"""
    paginate_by = 5
    model = Complaint

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        current_user_groups = self.request.user.groups.values_list("name", flat=True)
        context['is_manager'] = "Manager" in current_user_groups
        return context


class NewComplaint(View):
    """Complaint creation form"""
    def get(self, request):
        form = ComplaintForm()
        closing_user = User.objects.filter(groups__name='Manager').values_list("first_name", flat=True)
        info_alert = False
        context = {'form': form, 'closing_user': closing_user, 'info_alert': info_alert}
        return render(request, 'complaints/new_complaint.html', context)

    def post(self, request):
        form = ComplaintForm(request.POST)
        current_user = request.user
        closing_user = User.objects.filter(groups__name='Manager')
        error_approver = 'Approver must be different than reporting user'
        info_alert = False
        if form.is_valid():
            new_complaint = Complaint()
            new_complaint.cpl_name = form.cleaned_data.get('cpl_name')
            new_complaint.cpl_details = form.cleaned_data.get('cpl_details')
            new_complaint.cpl_deadline = form.cleaned_data.get('cpl_deadline')
            new_complaint.closing_user = form.cleaned_data.get('closing_user')
            new_complaint.reporting_user = current_user
            if new_complaint.is_approver_different_than_reporting_user():
                new_complaint.save()
                return HttpResponseRedirect(reverse('complaints:complaint_detail', args=(new_complaint.pk,)))
            else:
                info_alert = True
        context = {'form': form, 'closing_user': closing_user, 'error_approver': error_approver,
                   'info_alert': info_alert}
        return render(request, 'complaints/new_complaint.html', context)


def complaint_detail(request, complaint_id):
    """Detail page of selected complaint"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    selected_cpl = get_object_or_404(Complaint, pk=complaint_id)
    tasks_for_complaint = Task.objects.filter(complaint=complaint_id)
    context = {'selected_cpl': selected_cpl,
               'tasks_for_complaint': tasks_for_complaint,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/complaint_detail.html', context)


def my_complaints(request):
    """View of all complaints created by logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    my_cpl_list = cpls_created_by_me(current_user)
    count_of_my_cpl_list = count_of_cpls_created_by_me(current_user)
    context = {'my_cpl_list': my_cpl_list,
               'count_of_my_cpl_list': count_of_my_cpl_list,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/my_complaints.html', context)


def my_open_complaints(request):
    """View of open complaints created by logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    my_open_cpls = users_open_cpls(current_user)
    count_of_my_open_cpls = users_open_cpls_count(current_user)
    context = {'my_open_cpls': my_open_cpls,
               'count_of_my_open_cpls': count_of_my_open_cpls,
               "is_manager": "Manager" in current_user_groups}
    return render(request, 'complaints/my_open_complaints.html', context)


def my_closed_complaints(request):
    """View of closed complaints created by logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    my_closed_cpls = users_closed_cpls(current_user)
    count_of_my_closed_cpls = users_closed_cpls_count(current_user)
    context = {
        'count_of_my_closed_cpls': count_of_my_closed_cpls,
        'my_closed_cpls': my_closed_cpls,
        "is_manager": "Manager" in current_user_groups
    }
    return render(request, 'complaints/my_closed_complaints.html', context)


# Views for managers
def my_complaints_to_approve(request):
    """View of open complaints created by logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    my_not_approved_cpls = cpls_awaiting_approval(current_user)
    count_of_my_not_approved_cpls = cpls_awaiting_approval_count(current_user)
    context = {
        'my_not_approved_cpls': my_not_approved_cpls,
        'count_of_my_not_approved_cpls': count_of_my_not_approved_cpls,
        "is_manager": "Manager" in current_user_groups
               }
    return render(request, 'complaints/my_complaints_to_approve.html', context)


def my_approved_complaints(request):
    """View of open complaints created by logged in user"""
    # getting list of groups user belongs to for later determination if user belongs to admin
    current_user_groups = request.user.groups.values_list("name", flat=True)
    current_user = request.user.id
    my_approved_cpls = approved_cpls(current_user)
    count_of_my_approved_cpls = approved_cpls_count(current_user)
    context = {
        'my_approved_cpls': my_approved_cpls,
        'count_of_my_approved_cpls': count_of_my_approved_cpls,
        "is_manager": "Manager" in current_user_groups
               }
    return render(request, 'complaints/my_approved_complaints.html', context)


# TODO closing complaint view with validation - all tasks closed

