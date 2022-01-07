from django.urls import path
from .Views import cpl_views, tsk_views, base_views


app_name = 'complaints'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    path('complaints/', cpl_views.ComplaintListView.as_view(), name='complaint_list'),
    path('complaints/<int:complaint_id>', cpl_views.complaint_detail, name='complaint_detail'),
    path('new_complaint/', cpl_views.NewComplaint.as_view(), name='new_complaint'),
    path('complaints/my_complaints', cpl_views.my_complaints, name='my_complaints'),
    path('complaints/my_open_complaints', cpl_views.my_open_complaints, name='my_open_complaints'),
    path('complaints/my_closed_complaints', cpl_views.my_closed_complaints, name='my_closed_complaints'),
    path('complaints/my_complaints_to_approve', cpl_views.my_complaints_to_approve,
         name='my_complaints_to_approve'),
    path('complaints/my_approved_complaints', cpl_views.my_approved_complaints, name='my_approved_complaints'),
    path('complaints/<int:complaint_id>/new_task/', tsk_views.NewTask.as_view(), name='new_task'),
    path('tasks/my_tasks', tsk_views.my_tasks, name='my_tasks'),
    path('tasks/my_open_tasks', tsk_views.my_open_tasks, name='my_open_tasks'),
    path('tasks/my_closed_tasks', tsk_views.my_closed_tasks, name='my_closed_tasks'),
    path('tasks/<int:task_id>', tsk_views.task_detail, name='task_detail'),
    ]
