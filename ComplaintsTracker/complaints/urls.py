from django.urls import path
from .Views import cpl_views, tsk_views, base_views


app_name = 'complaints'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('dashboard/', base_views.dashboard, name='dashboard'),
    path('complaints/', cpl_views.ComplaintListView.as_view(), name='complaint_list'),
    path('complaints/<int:pk>', cpl_views.ComplaintDetailView.as_view(), name='complaint_detail'),
    ]
