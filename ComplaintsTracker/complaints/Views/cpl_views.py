from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ..Logic.cpl_logic import *


class ComplaintListView(ListView):
    """List view of all complaints created by all users"""
    paginate_by = 5
    model = Complaint


def complaint_detail(request, complaint_id):
    """Detail page of selected complaint"""
    selected_cpl = get_object_or_404(Complaint, pk=complaint_id)
    tasks_for_complaint = Task.objects.filter(complaint=complaint_id)
    context = {'selected_cpl': selected_cpl, 'tasks_for_complaint': tasks_for_complaint}
    return render(request, 'complaints/complaint_detail.html', context)


def my_complaints(request):
    """View of complaints created by logged in user"""
    current_user = request.user.id
    my_cpl_list = cpls_created_by_me(current_user)
    count_of_my_cpl_list = count_of_cpls_created_by_me(current_user)
    context = {'my_cpl_list': my_cpl_list, 'count_of_my_cpl_list': count_of_my_cpl_list}
    return render(request, 'complaints/my_complaints.html', context)

# TODO create complaint view
# TODO closing complaint view
